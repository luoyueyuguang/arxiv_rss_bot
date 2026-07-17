import sys

import run_all_bots


class SuccessfulBot:
    received_display_limit = None

    def __init__(self, display_limit=None):
        type(self).received_display_limit = display_limit

    def run(self):
        return [object(), object()]


class FailingBot:
    def __init__(self, display_limit=None):
        self.display_limit = display_limit

    def run(self):
        raise RuntimeError("upstream failed")


def test_run_all_reports_counts_and_forwards_display_limit(monkeypatch):
    monkeypatch.setattr(run_all_bots, "BOT_CLASSES", {"ok": SuccessfulBot})

    result = run_all_bots.run_all(["ok"], display_limit=17)

    assert result == {"ok": {"status": "ok", "count": 2}}
    assert SuccessfulBot.received_display_limit == 17


def test_run_all_records_individual_failures(monkeypatch):
    monkeypatch.setattr(
        run_all_bots,
        "BOT_CLASSES",
        {"ok": SuccessfulBot, "broken": FailingBot},
    )

    result = run_all_bots.run_all(["ok", "broken"])

    assert result["ok"]["status"] == "ok"
    assert result["broken"] == {
        "status": "error",
        "error": "upstream failed",
    }


def test_main_returns_nonzero_when_any_bot_fails(monkeypatch):
    monkeypatch.setattr(run_all_bots, "BOT_CLASSES", {"broken": FailingBot})
    monkeypatch.setattr(sys, "argv", ["run_all_bots.py", "broken"])

    assert run_all_bots.main() == 1


def test_main_returns_zero_on_success(monkeypatch):
    monkeypatch.setattr(run_all_bots, "BOT_CLASSES", {"ok": SuccessfulBot})
    monkeypatch.setattr(sys, "argv", ["run_all_bots.py", "ok"])

    assert run_all_bots.main() == 0

