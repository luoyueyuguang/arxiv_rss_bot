def test_deduplicates_by_id_title_and_link(bot_factory, paper_factory):
    bot = bot_factory()
    original = paper_factory(paper_id="one", title="Original")
    same_id = paper_factory(paper_id="one", title="Different")
    same_title = paper_factory(paper_id="two", title="Original")
    same_link = paper_factory(paper_id="three", title="Third")
    same_link["link"] = original["link"]
    unique = paper_factory(paper_id="four", title="Unique")

    result = bot.deduplicate_papers(
        [original, same_id, same_title, same_link, unique]
    )

    assert [paper["id"] for paper in result] == ["one", "four"]


def test_deduplication_preserves_input_order(bot_factory, paper_factory):
    bot = bot_factory()
    papers = [
        paper_factory(paper_id="two", title="Second"),
        paper_factory(paper_id="one", title="First"),
    ]

    assert bot.deduplicate_papers(papers) == papers


def test_deduplication_handles_empty_input(bot_factory):
    bot = bot_factory()

    assert bot.deduplicate_papers([]) == []
    assert bot.deduplicate_papers(None) is None


def test_deduplication_respects_configured_methods(
    bot_factory, base_config, paper_factory
):
    config = dict(base_config, deduplication_methods=["id"])
    bot = bot_factory(config)
    first = paper_factory(paper_id="one", title="Same Title")
    same_title = paper_factory(paper_id="two", title="Same Title")

    result = bot.deduplicate_papers([first, same_title])

    assert [paper["id"] for paper in result] == ["one", "two"]
