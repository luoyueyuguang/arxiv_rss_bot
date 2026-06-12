#!/usr/bin/env python3
"""
Run all conference bots to update their READMEs and caches.
"""

import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bots.arch_bot import ArchBot
from bots.hpc_bot import HPCBot
from bots.sys_bot import SysBot
from bots.chip_bot import ChipBot
from bots.ai_bot import AIBot
from bots.num_bot import NumBot

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

BOT_CLASSES = {
    "arch": ArchBot,
    "hpc": HPCBot,
    "sys": SysBot,
    "chip": ChipBot,
    "ai": AIBot,
    "num": NumBot,
}


def run_all(bots: list = None) -> dict:
    results = {}
    names = bots if bots else list(BOT_CLASSES.keys())

    for name in names:
        cls = BOT_CLASSES.get(name)
        if cls is None:
            logger.warning("Unknown bot: %s", name)
            continue
        logger.info("=" * 60)
        logger.info("Running %s bot...", name)
        try:
            bot_instance = cls()
            papers = bot_instance.run()
            results[name] = {"status": "ok", "count": len(papers)}
            logger.info("%s bot done: %d papers", name, len(papers))
        except Exception as exc:
            logger.error("%s bot failed: %s", name, exc)
            results[name] = {"status": "error", "error": str(exc)}
    return results


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Run conference bots")
    parser.add_argument(
        "bots",
        nargs="*",
        choices=list(BOT_CLASSES.keys()) + ["all"],
        default=["all"],
        help="Which bots to run (default: all)",
    )
    parser.add_argument(
        "--display-limit",
        type=int,
        default=100,
        help="Max papers to display per conference",
    )
    args = parser.parse_args()

    if "all" in args.bots:
        selected = list(BOT_CLASSES.keys())
    else:
        selected = args.bots

    results = run_all(selected)

    total = sum(r.get("count", 0) for r in results.values())
    errors = sum(1 for r in results.values() if r["status"] != "ok")
    logger.info("=" * 60)
    logger.info("Summary: %d papers across %d bots (%d errors)", total, len(results), errors)
    for name, r in results.items():
        if r["status"] == "ok":
            logger.info("  ✓ %s: %d papers", name, r["count"])
        else:
            logger.info("  ✗ %s: %s", name, r.get("error", "unknown"))


if __name__ == "__main__":
    main()
