import copy
import json
import sys
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from arxiv_bot import ArxivBot  # noqa: E402


def pytest_collection_modifyitems(items):
    """Classify legacy live checks without coupling them to pytest imports."""
    for item in items:
        parts = Path(str(item.path)).parts
        if "ai" in parts:
            item.add_marker(pytest.mark.integration)
        elif "services" in parts:
            item.add_marker(pytest.mark.rss)


@pytest.fixture
def base_config():
    return {
        "categories": ["cs.AI"],
        "keywords": ["machine learning", "transformer"],
        "high_score_keywords": [],
        "exclude_keywords": ["survey"],
        "max_papers": 10,
        "days_back": 7,
        "min_score": 0.0,
        "enable_deduplication": True,
        "ai_summary": {"enabled": False},
    }


@pytest.fixture
def bot_factory(tmp_path, base_config):
    def make_bot(config=None):
        effective_config = copy.deepcopy(config or base_config)
        config_path = tmp_path / "config.json"
        config_path.write_text(json.dumps(effective_config), encoding="utf-8")
        return ArxivBot(
            config_file=str(config_path),
            summary_cache_file=str(tmp_path / "summary_cache.json"),
        )

    return make_bot


@pytest.fixture
def paper_factory():
    def make_paper(
        paper_id="2607.00001v1",
        title="A Transformer for Machine Learning",
        summary="A machine learning paper.",
        paper_type="new",
        category="cs.AI",
    ):
        return {
            "id": paper_id,
            "arxiv_id": paper_id,
            "title": title,
            "authors": ["Author A"],
            "type": paper_type,
            "summary": summary,
            "category": category,
            "published_date": "2026-07-01",
            "link": f"https://arxiv.org/abs/{paper_id}",
            "score": 0.0,
        }

    return make_paper
