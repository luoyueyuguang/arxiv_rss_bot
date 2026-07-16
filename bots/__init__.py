#!/usr/bin/env python3
"""
Conference bots __init__.
"""

from bots.arch_bot import ArchBot
from bots.hpc_bot import HPCBot
from bots.sys_bot import SysBot
from bots.chip_bot import ChipBot
from bots.ai_bot import AIBot
from bots.num_bot import NumBot
from bots.iclr_bot import ICLRBot

__all__ = [
    "ArchBot", "HPCBot", "SysBot", "ChipBot", "AIBot", "NumBot", "ICLRBot"
]
