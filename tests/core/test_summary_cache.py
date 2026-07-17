import json


def _enable_ai(bot):
    bot.config["ai_summary"] = {
        "enabled": True,
        "api_key_env": "TEST_AI_API_KEY",
        "base_url": "https://example.invalid/v1",
        "model": "test-model",
        "prompt_file": "ai_summary_prompt.txt",
        "max_papers_to_summarize": 10,
        "max_workers": 1,
        "use_pdf": False,
    }


def _cache_entry(bot, summary):
    return {
        **bot._summary_cache_identity(bot.config["ai_summary"]),
        "summary": summary,
        "generated_at": "2026-07-01T00:00:00+00:00",
    }


def test_cache_hit_reuses_summary_without_processing(
    monkeypatch, bot_factory, paper_factory
):
    bot = bot_factory()
    _enable_ai(bot)
    cache_path = bot.summary_cache_file
    with open(cache_path, "w", encoding="utf-8") as cache_file:
        json.dump({"2607.00001v1": _cache_entry(bot, "Cached summary")}, cache_file)

    def fail_if_called(*_args, **_kwargs):
        raise AssertionError("cached paper should not be processed")

    monkeypatch.setattr(bot, "_process_paper_with_ai", fail_if_called)

    section = bot.generate_papers_section([paper_factory()])

    assert "Cached summary" in section


def test_cache_miss_processes_and_persists_summary(
    monkeypatch, bot_factory, paper_factory
):
    bot = bot_factory()
    _enable_ai(bot)

    def summarize(_paper, index, _config, _client):
        return index, "New summary"

    monkeypatch.setattr(bot, "_process_paper_with_ai", summarize)

    section = bot.generate_papers_section([paper_factory()])

    assert "New summary" in section
    with open(bot.summary_cache_file, encoding="utf-8") as cache_file:
        saved = json.load(cache_file)["2607.00001v1"]
    assert saved["summary"] == "New summary"
    assert saved["model"] == "test-model"
    assert saved["mode"] == "abstract"
    assert len(saved["prompt_hash"]) == 64


def test_mixed_cache_only_processes_missing_paper(
    monkeypatch, bot_factory, paper_factory
):
    bot = bot_factory()
    _enable_ai(bot)
    with open(bot.summary_cache_file, "w", encoding="utf-8") as cache_file:
        json.dump({"one": _cache_entry(bot, "Cached one")}, cache_file)
    processed = []

    def summarize(paper, index, _config, _client):
        processed.append(paper["arxiv_id"])
        return index, "Fresh two"

    monkeypatch.setattr(bot, "_process_paper_with_ai", summarize)
    papers = [
        paper_factory(paper_id="one", title="Paper One"),
        paper_factory(paper_id="two", title="Paper Two"),
    ]

    section = bot.generate_papers_section(papers)

    assert processed == ["two"]
    assert "Cached one" in section
    assert "Fresh two" in section


def test_legacy_cache_is_invalidated(monkeypatch, bot_factory, paper_factory):
    bot = bot_factory()
    _enable_ai(bot)
    with open(bot.summary_cache_file, "w", encoding="utf-8") as cache_file:
        json.dump({"2607.00001v1": "legacy summary"}, cache_file)
    processed = []

    def summarize(paper, index, _config, _client):
        processed.append(paper["arxiv_id"])
        return index, "regenerated"

    monkeypatch.setattr(bot, "_process_paper_with_ai", summarize)

    section = bot.generate_papers_section([paper_factory()])

    assert processed == ["2607.00001v1"]
    assert "regenerated" in section
    assert "legacy summary" not in section


def test_model_change_invalidates_structured_cache(
    monkeypatch, bot_factory, paper_factory
):
    bot = bot_factory()
    _enable_ai(bot)
    old_entry = _cache_entry(bot, "old model summary")
    old_entry["model"] = "old-model"
    with open(bot.summary_cache_file, "w", encoding="utf-8") as cache_file:
        json.dump({"2607.00001v1": old_entry}, cache_file)
    monkeypatch.setattr(
        bot,
        "_process_paper_with_ai",
        lambda _paper, index, _config, _client: (index, "new model summary"),
    )

    section = bot.generate_papers_section([paper_factory()])

    assert "new model summary" in section
    assert "old model summary" not in section


def test_disabled_ai_does_not_read_cache(bot_factory, paper_factory):
    bot = bot_factory()
    with open(bot.summary_cache_file, "w", encoding="utf-8") as cache_file:
        json.dump({"2607.00001v1": "Must not appear"}, cache_file)

    section = bot.generate_papers_section([paper_factory()])

    assert "Must not appear" not in section
    assert "AI Summary" not in section


def test_corrupt_cache_is_treated_as_empty(
    monkeypatch, bot_factory, paper_factory
):
    bot = bot_factory()
    _enable_ai(bot)
    with open(bot.summary_cache_file, "w", encoding="utf-8") as cache_file:
        cache_file.write("not-json")
    monkeypatch.setattr(
        bot,
        "_process_paper_with_ai",
        lambda _paper, index, _config, _client: (index, None),
    )

    section = bot.generate_papers_section([paper_factory()])

    assert "A Transformer for Machine Learning" in section
    with open(bot.summary_cache_file, encoding="utf-8") as cache_file:
        assert json.load(cache_file) == {}
