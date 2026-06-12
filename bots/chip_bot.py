#!/usr/bin/env python3
"""
Chip / EDA Conference Bot
Covers: DAC, ICCAD, DATE, VLSI Symposium, ISPD
Primary: arXiv cs.AR, cs.ET with conference name matching
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import logging
from base_conference_bot import BaseConferenceBot

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class ChipBot(BaseConferenceBot):
    NAME = "chip"
    CONFERENCE_NAME = "Chip Design / EDA"
    OUTPUT_DIR = "conferences/chip"
    DAYS_BACK = 7

    ARXIV_CATEGORIES = ["cs.AR"]

    CONFERENCE_NAME_KEYWORDS = [
        "DAC", "Design Automation Conference",
        "ICCAD", "International Conference on Computer-Aided Design",
        "DATE", "Design Automation and Test in Europe",
        "VLSI Symposium", "Symposium on VLSI",
        "ISPD", "International Symposium on Physical Design",
        "ASPDAC", "Asia and South Pacific Design Automation",
        "FPGA", "International Symposium on Field-Programmable Gate Arrays",
    ]

    HIGH_SCORE_KEYWORDS = [
        "Placement", "Routing", "Place and route",
        "Logic synthesis", "High-level synthesis",
        "Static timing analysis", "Clock tree synthesis",
        "Design for test", "Design for manufacturability",
        "Standard cell", "Standard cell library",
        "Physical design", "Floorplanning",
        "Power grid", "IR drop",
        "Chiplet", "Through-silicon via",
        "3D IC", "Heterogeneous integration",
        "OpenROAD", "Yosys",
        "ML for EDA", "RL placement",
    ]

    @property
    def conference_keywords(self) -> list:
        return [
            "EDA", "electronic design automation",
            "VLSI", "ASIC", "FPGA", "chip design",
            "place", "route", "placement", "routing",
            "logic synthesis", "high-level synthesis",
            "physical design", "floorplan",
            "timing", "static timing", "STA",
            "clock", "clock tree", "CTS",
            "power", "power grid", "IR drop",
            "design for manufacturability", "DFM",
            "design for test", "DFT", "scan",
            "RTL", "register transfer",
            "verification", "formal verification",
            "simulation", "emulation", "FPGA prototyping",
            "analog", "mixed-signal", "AMS",
            "memory compiler", "SRAM generator",
            "standard cell", "standard cell library",
            "technology node", "FinFET", "GAA",
            "interconnect", "wire", "parasitic",
            "machine learning for EDA", "ML for EDA",
            "AI for chip", "reinforcement learning placement",
            "thermal", "package", "PCB",
            "SystemVerilog", "Verilog", "VHDL",
            "3D IC", "through-silicon via", "TSV",
            "chiplet", "heterogeneous integration",
            "open-source EDA", "OpenROAD", "Yosys",
            "process design kit", "PDK",
        ]


def main():
    bot = ChipBot()
    try:
        papers = bot.run()
        logger.info("Chip Bot: %d papers", len(papers))
    except Exception as exc:
        logger.error("Chip Bot failed: %s", exc)
        raise


if __name__ == "__main__":
    main()
