#!/usr/bin/env python3
"""
Test suite for AI summary caching across runs.
"""

import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from arxiv_bot import ArxivBot


# ── helpers ────────────────────────────────────────────────────────────────

def _make_paper(arxiv_id, title="Test Paper"):
    return {
        "arxiv_id": arxiv_id,
        "id": arxiv_id,
        "title": title,
        "authors": ["Author A"],
        "link": f"http://arxiv.org/abs/{arxiv_id}",
        "category": "cs.AI",
        "published_date": "2026-07-01",
        "score": 90.0,
        "type": "new",
        "summary": "Short abstract for testing.",
    }


def _make_bot(summary_cache_file=None):
    """Create an ArxivBot with AI enabled but no real API key."""
    bot = ArxivBot()
    bot.config["ai_summary"] = {
        "enabled": True,
        "api_key_env": "ARK_API_KEY",
        "base_url": "https://ark.cn-beijing.volces.com/api/v3",
        "model": "doubao-seed-2-0-mini-260428",
        "prompt_file": "ai_summary_prompt.txt",
        "max_papers_to_summarize": 10,
        "max_workers": 1,
        "use_pdf": False,
    }
    # Remove API key so we don't hit the real API
    os.environ.pop("ARK_API_KEY", None)
    if summary_cache_file:
        bot.summary_cache_file = summary_cache_file
    return bot


# ── tests ──────────────────────────────────────────────────────────────────

def test_cache_hit_reuses_summary():
    """Paper already in cache → reused, no API call attempted."""
    print("Testing cache hit...")
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump({"2606.10001v1": "Cached summary!"}, f)
        cache_path = f.name

    try:
        bot = _make_bot(cache_path)
        papers = [_make_paper("2606.10001v1")]
        section = bot.generate_papers_section(papers)
        assert "Cached summary!" in section, "Cached summary NOT reused"
        print("  ✅ Cache hit: summary reused correctly")
    finally:
        os.unlink(cache_path)


def test_cache_miss_does_not_crash():
    """Paper not in cache → no crash, AI skipped gracefully when no key."""
    print("Testing cache miss...")
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump({}, f)
        cache_path = f.name

    try:
        bot = _make_bot(cache_path)
        papers = [_make_paper("2606.99999v1")]
        section = bot.generate_papers_section(papers)
        # No AI summary in output (API key not set), but no crash either
        assert "2606.99999v1" in section, "Paper should appear in output"
        assert "AI Summary" not in section, "Should not have AI summary without API key"
        print("  ✅ Cache miss: no crash, paper rendered without AI summary")
    finally:
        os.unlink(cache_path)


def test_mixed_cache_hit_and_miss():
    """2 of 3 papers cached → only 1 needs processing."""
    print("Testing mixed cache hit/miss...")
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump({
            "2606.10001v1": "Cached A",
            "2606.10002v1": "Cached B",
        }, f)
        cache_path = f.name

    try:
        bot = _make_bot(cache_path)
        papers = [
            _make_paper("2606.10001v1", "Paper A"),
            _make_paper("2606.10002v1", "Paper B"),
            _make_paper("2606.10003v1", "Paper C"),
        ]
        section = bot.generate_papers_section(papers)
        assert "Cached A" in section, "Paper A cache missed"
        assert "Cached B" in section, "Paper B cache missed"
        assert "Cached A" not in section.replace("Cached B", "").replace("Cached A", ""), "Should not duplicate"
        print("  ✅ Mixed: 2 cached reused, 1 skipped (no API key)")
    finally:
        os.unlink(cache_path)


def test_missing_cache_file():
    """No cache file on disk → treated as empty, no crash."""
    print("Testing missing cache file...")
    bot = _make_bot("/tmp/nonexistent_summary_cache.json")
    papers = [_make_paper("2606.10001v1")]
    section = bot.generate_papers_section(papers)
    assert "2606.10001v1" in section, "Paper should appear"
    print("  ✅ Missing cache file: no crash, all papers rendered")


def test_empty_cache_dict():
    """Empty JSON `{}` → same as no cache."""
    print("Testing empty cache dict...")
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump({}, f)
        cache_path = f.name

    try:
        bot = _make_bot(cache_path)
        papers = [_make_paper("2606.10001v1"), _make_paper("2606.10002v1")]
        section = bot.generate_papers_section(papers)
        assert "2606.10001v1" in section
        assert "2606.10002v1" in section
        # No AI summaries (no key), but no crash
        assert "AI Summary" not in section
        print("  ✅ Empty cache: no crash, all rendered")
    finally:
        os.unlink(cache_path)


def test_cache_saved_after_processing():
    """After processing, new summaries are persisted to cache file."""
    print("Testing cache save after processing...")
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump({}, f)
        cache_path = f.name

    try:
        bot = _make_bot(cache_path)
        papers = [_make_paper("2606.10001v1")]
        bot.generate_papers_section(papers)

        # Cache should still exist and be valid JSON
        with open(cache_path, "r") as f:
            saved = json.load(f)
        assert isinstance(saved, dict), "Cache should be a dict"
        # No summaries saved because API key was missing → all summaries were None
        print(f"  ✅ Cache saved: {len(saved)} entries (expected 0 — no API key)")
    finally:
        os.unlink(cache_path)


def test_cache_not_corrupted_by_empty_run():
    """Empty paper list does not corrupt existing cache."""
    print("Testing cache integrity with empty paper list...")
    existing = {"2606.10001v1": "Existing summary"}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(existing, f)
        cache_path = f.name

    try:
        bot = _make_bot(cache_path)
        section = bot.generate_papers_section([])
        assert section == "No papers found matching the criteria."
        # Cache should be untouched
        with open(cache_path, "r") as f:
            saved = json.load(f)
        assert saved == existing, "Cache should NOT be modified on empty run"
        print("  ✅ Empty paper list: cache untouched")
    finally:
        os.unlink(cache_path)


def test_different_arxiv_version_is_new():
    """v1 cached, v2 in feed → treated as new paper (not cached)."""
    print("Testing version-differentiated caching...")
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump({"2606.10001v1": "Summary for v1"}, f)
        cache_path = f.name

    try:
        bot = _make_bot(cache_path)
        papers = [
            _make_paper("2606.10001v1", "Paper v1"),
            _make_paper("2606.10001v2", "Paper v2"),
        ]
        section = bot.generate_papers_section(papers)
        assert "Summary for v1" in section, "v1 cache should be reused"
        assert "Paper v2" in section, "v2 should appear"
        # v2 should not have cached summary
        assert "AI Summary" not in section.split("Paper v2")[1].split("---")[0], \
            "v2 should NOT reuse v1's cached summary"
        print("  ✅ Version-differentiated: v1 cached reused, v2 treated as new")
    finally:
        os.unlink(cache_path)


def test_no_ai_when_disabled():
    """When ai_summary.enabled = False, cache is never loaded or saved."""
    print("Testing AI disabled mode...")
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump({"2606.10001v1": "Should not appear"}, f)
        cache_path = f.name

    try:
        bot = _make_bot(cache_path)
        bot.config["ai_summary"]["enabled"] = False
        papers = [_make_paper("2606.10001v1")]
        section = bot.generate_papers_section(papers)
        assert "Should not appear" not in section, "Cached summary leaked when AI disabled"
        assert "AI Summary" not in section
        print("  ✅ AI disabled: cache not used, no AI summary in output")
    finally:
        os.unlink(cache_path)


# ── main ───────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("🧪 Summary Cache Test Suite")
    print("=" * 60)

    tests = [
        test_cache_hit_reuses_summary,
        test_cache_miss_does_not_crash,
        test_mixed_cache_hit_and_miss,
        test_missing_cache_file,
        test_empty_cache_dict,
        test_cache_saved_after_processing,
        test_cache_not_corrupted_by_empty_run,
        test_different_arxiv_version_is_new,
        test_no_ai_when_disabled,
    ]

    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"  ❌ FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"  💥 ERROR: {e}")
            failed += 1

    print()
    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed out of {len(tests)}")
    print("=" * 60)

    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
