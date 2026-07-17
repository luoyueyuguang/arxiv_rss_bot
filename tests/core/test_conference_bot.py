import json

import pytest
import requests

from base_conference_bot import (
    BaseConferenceBot,
    ConferencePaper,
    _keyword_matches,
)
from bots.iclr_bot import ICLRBot


class DummyConferenceBot(BaseConferenceBot):
    NAME = "dummy"
    CONFERENCE_NAME = "Dummy Conference"
    OUTPUT_DIR = "unused"
    ARXIV_CATEGORIES = ["cs.AI"]
    HIGH_SCORE_KEYWORDS = ["accelerator"]

    @property
    def conference_keywords(self):
        return ["distributed system", "GPU"]


def make_paper(title, abstract=""):
    return ConferencePaper(
        forum_id=title,
        paper_number=1,
        title=title,
        authors=["Author"],
        keywords=[],
        abstract=abstract,
        pdf_link=None,
        forum_link="https://example.invalid/paper",
        submission_date=None,
        conference="Dummy",
    )


def test_conference_config_overrides_display_limit(tmp_path):
    config_path = tmp_path / "config.json"
    config_path.write_text(
        json.dumps({"conferences": {"dummy": {"display_limit": 23}}}),
        encoding="utf-8",
    )

    bot = DummyConferenceBot(config_file=str(config_path), output_dir=tmp_path)

    assert bot.display_limit == 23


def test_conference_config_applies_operational_settings(tmp_path):
    config_path = tmp_path / "config.json"
    config_path.write_text(
        json.dumps(
            {
                "fetch_ratings": True,
                "conferences": {
                    "dummy": {
                        "year": 2030,
                        "display_limit": 23,
                        "cache_limit": 42,
                        "min_score": 2.5,
                        "fetch_ratings": False,
                        "days_back": 14,
                    }
                },
            }
        ),
        encoding="utf-8",
    )

    bot = DummyConferenceBot(config_file=str(config_path), output_dir=tmp_path)

    assert bot.year == 2030
    assert bot.cache_limit == 42
    assert bot.min_score == 2.5
    assert bot.fetch_ratings is False
    assert bot.days_back == 14


def test_conference_filter_and_score_are_configurable(tmp_path):
    config_path = tmp_path / "config.json"
    config_path.write_text(
        json.dumps(
            {
                "exclude_keywords": ["survey"],
                "conferences": {
                    "dummy": {"keywords": ["compiler", "accelerator"]}
                },
            }
        ),
        encoding="utf-8",
    )
    bot = DummyConferenceBot(config_file=str(config_path), output_dir=tmp_path)
    accepted = make_paper("An Accelerator Compiler")
    excluded = make_paper("Accelerator Survey")

    assert bot.matches_criteria(accepted) is True
    assert bot.matches_criteria(excluded) is False
    assert bot.calculate_score(accepted) > 0


def test_conference_readme_handles_empty_result(tmp_path):
    config_path = tmp_path / "config.json"
    config_path.write_text('{"fetch_ratings": false}', encoding="utf-8")
    bot = DummyConferenceBot(config_file=str(config_path), output_dir=tmp_path)

    rendered = bot.render_readme([])

    assert "Total Filtered Papers**: 0" in rendered
    assert "No papers matched" in rendered


def test_short_keywords_require_token_boundaries():
    assert _keyword_matches("RDMA and IR optimization", "IR") is True
    assert _keyword_matches("first principles", "IR") is False
    assert _keyword_matches("a new shirt", "IR") is False


def test_formal_source_wins_title_deduplication():
    arxiv = make_paper("Same Paper", "arxiv abstract")
    arxiv.source = "arxiv"
    arxiv.forum_id = "arxiv-id"
    openreview = make_paper("Same Paper", "openreview abstract")
    openreview.source = "openreview"
    openreview.forum_id = "openreview-id"

    merged = BaseConferenceBot._merge_papers_by_title([arxiv, openreview])

    assert len(merged) == 1
    assert merged[0].source == "openreview"
    assert merged[0].forum_id == "openreview-id"


def test_empty_fetch_preserves_existing_cache(monkeypatch, tmp_path):
    config_path = tmp_path / "config.json"
    config_path.write_text("{}", encoding="utf-8")
    bot = DummyConferenceBot(config_file=str(config_path), output_dir=tmp_path)
    bot.save_cache([make_paper("Existing System Paper", "system")])
    monkeypatch.setattr(bot, "fetch_papers", lambda: [])

    with pytest.raises(RuntimeError, match="produced no papers"):
        bot.run()

    cached = json.loads(bot.cache_path.read_text(encoding="utf-8"))
    assert cached["paper_count"] == 1
    assert cached["papers"][0]["title"] == "Existing System Paper"


def test_unchanged_paper_preserves_updated_at(tmp_path):
    config_path = tmp_path / "config.json"
    config_path.write_text("{}", encoding="utf-8")
    bot = DummyConferenceBot(config_file=str(config_path), output_dir=tmp_path)
    bot.save_cache([make_paper("Stable System Paper", "system")])
    first = json.loads(bot.cache_path.read_text(encoding="utf-8"))

    bot.save_cache([make_paper("Stable System Paper", "system")])
    second = json.loads(bot.cache_path.read_text(encoding="utf-8"))

    assert second["papers"][0]["updated_at"] == first["papers"][0]["updated_at"]


def test_markdown_table_escapes_pipe(tmp_path):
    config_path = tmp_path / "config.json"
    config_path.write_text("{}", encoding="utf-8")
    bot = DummyConferenceBot(config_file=str(config_path), output_dir=tmp_path)

    rendered = bot.render_readme([make_paper("A | B System", "system")])

    assert "A \\| B System" in rendered


def test_iclr_is_thin_configured_conference_bot(tmp_path):
    config_path = tmp_path / "config.json"
    config_path.write_text(
        json.dumps({"conferences": {"iclr": {"year": 2031}}}),
        encoding="utf-8",
    )

    bot = ICLRBot(config_file=str(config_path), output_dir=tmp_path)

    assert isinstance(bot, BaseConferenceBot)
    assert bot.year == 2031
    assert bot.OPENREVIEW_DOMAINS == ["ICLR.cc/2031/Conference"]
    assert bot.ARXIV_CATEGORIES == []


def test_all_configured_sources_failing_is_an_error(monkeypatch, tmp_path):
    config_path = tmp_path / "config.json"
    config_path.write_text("{}", encoding="utf-8")
    bot = DummyConferenceBot(config_file=str(config_path), output_dir=tmp_path)
    monkeypatch.setattr(
        bot,
        "fetch_papers_arxiv",
        lambda: (_ for _ in ()).throw(RuntimeError("offline")),
    )

    with pytest.raises(RuntimeError, match="All data sources failed"):
        bot.fetch_papers()


def test_failed_source_reuses_its_cached_records(monkeypatch, tmp_path):
    config_path = tmp_path / "config.json"
    config_path.write_text('{"fetch_ratings": false}', encoding="utf-8")
    bot = DummyConferenceBot(config_file=str(config_path), output_dir=tmp_path)
    bot.OPENREVIEW_DOMAINS = ["Demo/2030"]
    cached = make_paper("Cached OpenReview Distributed System", "distributed system")
    cached.source = "openreview"
    bot.save_cache([cached])
    fresh = make_paper("Fresh arXiv Distributed System", "distributed system")
    monkeypatch.setattr(bot, "fetch_papers_arxiv", lambda: [fresh])
    monkeypatch.setattr(
        bot,
        "fetch_papers_openreview",
        lambda: (_ for _ in ()).throw(requests.ConnectionError("offline")),
    )

    papers = bot.fetch_papers()

    assert {paper.source for paper in papers} == {"arxiv", "openreview"}


def test_conference_min_score_is_enforced(monkeypatch, tmp_path):
    config_path = tmp_path / "config.json"
    config_path.write_text(
        json.dumps({"conferences": {"dummy": {"min_score": 2.0}}}),
        encoding="utf-8",
    )
    bot = DummyConferenceBot(config_file=str(config_path), output_dir=tmp_path)
    low_score = make_paper("Distributed System", "")
    monkeypatch.setattr(bot, "fetch_papers_arxiv", lambda: [low_score])

    assert bot.fetch_papers() == []
