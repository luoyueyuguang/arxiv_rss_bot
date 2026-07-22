#!/usr/bin/env python3
"""ICLR conference bot backed by OpenReview."""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Optional

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base_conference_bot import BaseConferenceBot


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class ICLRBot(BaseConferenceBot):
    NAME = "iclr"
    CONFERENCE_NAME = "ICLR"
    OUTPUT_DIR = "conferences/iclr"
    ARXIV_CATEGORIES = []
    DAYS_BACK = 365

    HIGH_SCORE_KEYWORDS = [
        "sparse attention",
        "speculative decoding",
        "reinforcement learning",
        "large language model",
        "mixture of experts",
        "multimodal",
        "reasoning",
        # AI Agent
        "AI agent",
        "LLM agent",
        "autonomous agent",
        "multi-agent",
        "agentic",
        "tool use",
        "function calling",
        "agent planning",
        "task decomposition",
        "agent memory",
        "agent reflection",
        "self-improvement",
        "chain-of-thought",
        "in-context learning",
        # LLM principles
        "pretraining",
        "pre-training",
        "scaling law",
        "scaling laws",
        "emergent",
        "attention mechanism",
        "transformer architecture",
        "tokenization",
        "positional encoding",
        "next-token prediction",
        "language modeling",
        "mechanistic interpretability",
        "circuit analysis",
        "probing",
        "representation engineering",
        "knowledge distillation",
        "model compression",
        "model merging",
        "weight averaging",
    ]

    def __init__(
        self,
        year: Optional[int] = None,
        output_dir: Optional[Path] = None,
        max_papers: Optional[int] = None,
        display_limit: Optional[int] = None,
        session: Optional[requests.Session] = None,
        config_file: str = "config.json",
        days_back: Optional[int] = None,
    ) -> None:
        super().__init__(
            year=year,
            output_dir=output_dir,
            max_papers=max_papers,
            display_limit=display_limit,
            session=session,
            config_file=config_file,
            days_back=days_back,
        )
        self.allow_empty_result = True  # OpenReview may be unavailable
        self.CONFERENCE_NAME = f"ICLR {self.year}"
        self.OPENREVIEW_DOMAINS = [f"ICLR.cc/{self.year}/Conference"]

    @property
    def conference_keywords(self) -> list[str]:
        return [
            "large language model",
            "LLM",
            "transformer",
            "attention",
            "reinforcement learning",
            "RLHF",
            "inference",
            "training",
            "mixture of experts",
            "MoE",
            "quantization",
            "distributed",
            "multimodal",
            "reasoning",
            "diffusion",
            "graph neural network",
            "self-supervised",
            "representation learning",
        ]


def main() -> None:
    bot = ICLRBot()
    papers = bot.run()
    logger.info("ICLR Bot completed successfully with %d papers", len(papers))


if __name__ == "__main__":
    main()
