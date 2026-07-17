from datetime import datetime, timezone
from types import SimpleNamespace

import pytest

import arxiv_bot


def test_loads_explicit_config(bot_factory, base_config):
    bot = bot_factory()

    assert bot.config == base_config


def test_parse_recent_entry_uses_utc(bot_factory):
    bot = bot_factory()
    now = datetime.now(timezone.utc)
    entry = SimpleNamespace(
        link="https://arxiv.org/abs/2607.00001v1",
        title="A Transformer Paper",
        authors=[SimpleNamespace(name="Author A")],
        published_parsed=now.timetuple(),
        summary=(
            "arXiv:2607.00001v1 Announce Type: new "
            "Abstract: A machine learning paper."
        ),
    )

    paper = bot.parse_paper_entry(entry, "cs.AI")

    assert paper is not None
    assert paper["arxiv_id"] == "2607.00001v1"
    assert paper["type"] == "new"
    assert paper["published_date"] == now.strftime("%Y-%m-%d")


def test_parse_summary_preserves_multiline_abstract(bot_factory):
    parsed = bot_factory().parse_paper_summary(
        "arXiv:2607.00001v1 Announce Type: new "
        "Abstract: first line\nsecond line"
    )

    assert parsed == ("2607.00001v1", "new", "first line\nsecond line")


def test_filter_enforces_min_score_and_sorts(bot_factory, base_config, paper_factory):
    config = dict(base_config, min_score=2.0)
    bot = bot_factory(config)
    low_score = paper_factory(
        paper_id="low",
        title="Machine Learning Only",
        summary="No other configured term.",
    )
    high_score = paper_factory(
        paper_id="high",
        title="Transformer for Machine Learning",
        summary="Relevant work.",
    )

    filtered = bot.filter_papers([low_score, high_score])

    assert [paper["id"] for paper in filtered] == ["high"]
    assert filtered[0]["score"] == 3.0


@pytest.mark.parametrize(
    ("paper_type", "summary"),
    [("replace", "machine learning"), ("new", "machine learning survey")],
)
def test_filter_rejects_non_new_and_excluded_papers(
    bot_factory, paper_factory, paper_type, summary
):
    bot = bot_factory()
    paper = paper_factory(paper_type=paper_type, summary=summary)

    assert bot.filter_papers([paper]) == []


def test_fetch_deduplicates_across_categories(
    monkeypatch, bot_factory, base_config
):
    config = dict(base_config, categories=["cs.AI", "cs.LG"])
    bot = bot_factory(config)
    now = datetime.now(timezone.utc).timetuple()
    entry = SimpleNamespace(
        link="https://arxiv.org/abs/2607.00001v1",
        title="A Transformer Paper",
        authors=[SimpleNamespace(name="Author A")],
        published_parsed=now,
        summary=(
            "arXiv:2607.00001v1 Announce Type: new "
            "Abstract: A machine learning paper."
        ),
    )
    feed = SimpleNamespace(bozo=False, entries=[entry])
    requested_urls = []

    def parse(url):
        requested_urls.append(url)
        return feed

    monkeypatch.setattr(arxiv_bot.feedparser, "parse", parse)

    papers = bot.fetch_arxiv_papers()

    assert len(papers) == 1
    assert bot.last_fetch_succeeded is True
    assert requested_urls == [
        "https://export.arxiv.org/rss/cs.AI",
        "https://export.arxiv.org/rss/cs.LG",
    ]


def test_fetch_raises_when_every_feed_fails(monkeypatch, bot_factory):
    bot = bot_factory()
    failed_feed = SimpleNamespace(
        bozo=True,
        bozo_exception=RuntimeError("network down"),
        entries=[],
    )
    monkeypatch.setattr(arxiv_bot.feedparser, "parse", lambda _url: failed_feed)

    with pytest.raises(RuntimeError, match="All configured arXiv feeds failed"):
        bot.fetch_arxiv_papers()


def test_run_updates_readme_for_a_successful_empty_fetch(
    monkeypatch, bot_factory, tmp_path
):
    bot = bot_factory()
    monkeypatch.setattr(bot, "fetch_arxiv_papers", lambda: [])
    monkeypatch.chdir(tmp_path)

    result = bot.run()

    assert result == []
    readme = (tmp_path / "README.md").read_text(encoding="utf-8")
    assert "Total Papers Found**: 0" in readme
    assert "No papers matching the criteria" in readme


def test_rendered_timestamp_is_explicitly_utc(bot_factory):
    readme = bot_factory().render_readme([])

    assert "UTC" in readme


def test_pdf_mode_falls_back_to_abstract(monkeypatch, bot_factory, paper_factory):
    bot = bot_factory()
    monkeypatch.setattr(bot, "download_arxiv_pdf", lambda _paper: None)
    monkeypatch.setattr(
        bot,
        "summarize_text_with_ai",
        lambda title, abstract, client: f"fallback: {title}: {abstract}",
    )

    index, summary = bot._process_paper_with_ai(
        paper_factory(), 1, {"use_pdf": True}, None
    )

    assert index == 1
    assert summary.startswith("fallback:")
