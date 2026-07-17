import os

import pytest

from arxiv_bot import ArxivBot


@pytest.fixture(scope="module")
def live_bot():
    bot = ArxivBot()
    bot.config["categories"] = ["cs.AI"]
    bot.config["days_back"] = 7
    return bot


@pytest.fixture(scope="module")
def live_paper(live_bot):
    papers = live_bot.fetch_arxiv_papers()
    assert papers, "arXiv returned no recent cs.AI papers"
    return papers[0]


def test_live_arxiv_fetch(live_paper):
    assert live_paper["arxiv_id"]
    assert live_paper["link"].startswith("https://arxiv.org/abs/")


def test_live_pdf_download(live_bot, live_paper, tmp_path):
    pdf_path = live_bot.download_arxiv_pdf(live_paper, output_dir=tmp_path)

    assert pdf_path is not None
    assert pdf_path.read_bytes().startswith(b"%PDF-")


def test_live_ai_summary(live_bot, live_paper):
    ai_config = live_bot.config.get("ai_summary", {})
    api_key_env = ai_config.get("api_key_env", "ARK_API_KEY")
    if not os.environ.get(api_key_env):
        pytest.skip(f"{api_key_env} is not configured")
    ai_config["enabled"] = True

    summary = live_bot.summarize_text_with_ai(
        live_paper["title"], live_paper["summary"]
    )

    assert summary and len(summary.strip()) > 100
