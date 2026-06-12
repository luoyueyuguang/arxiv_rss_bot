#!/usr/bin/env python3
"""
Architecture Conference Bot
Covers: ISCA, MICRO, ASPLOS, HPCA — plus RISC-V focused venues
Primary: arXiv cs.AR (architecture), cs.DC, cs.PF
These conferences do NOT use OpenReview — fetched via arXiv with conference name matching.
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


class ArchBot(BaseConferenceBot):
    NAME = "arch"
    CONFERENCE_NAME = "Computer Architecture"
    OUTPUT_DIR = "conferences/arch"
    DAYS_BACK = 7

    ARXIV_CATEGORIES = ["cs.AR"]

    CONFERENCE_NAME_KEYWORDS = [
        "ISCA", "MICRO", "ASPLOS", "HPCA",
        "International Symposium on Computer Architecture",
        "International Symposium on Microarchitecture",
        "Architectural Support for Programming Languages and Operating Systems",
        "High Performance Computer Architecture",
        "CARRV", "Computer Architecture Research with RISC-V",
        "RISC-V Summit", "RISC-V International",
    ]

    HIGH_SCORE_KEYWORDS = [
        "Dataflow", "CGRA", "Near-memory", "Processing-in-memory",
        "Chiplet", "NoC", "Network-on-Chip", "Interconnect", "Cache coherence",
        "Branch predictor", "Prefetcher", "Out-of-order",
        "Tensor core", "Systolic array", "TPU", "GPU architecture",
        "SIMT", "Warp", "Vector processor", "SIMD",
        "RISC-V", "x86", "ARM", "Domain-specific",
        "Accelerator", "FPGA", "Reconfigurable",
        "DRAM", "HBM", "DDR", "CXL", "NVMe",
        "Power", "Energy", "Thermal",
        "Reliability", "Fault tolerance", "Security",
        # RISC-V
        "RISC-V processor", "RISC-V core",
        "RISC-V vector", "RVV", "Vector extension",
        "RISC-V custom", "Custom instruction",
        "RISC-V ISA", "ISA extension",
        "XiangShan", "Xiangshan",
        "BOOM", "SonicBOOM", "Rocket chip",
        "Spike simulator", "RISC-V simulator",
        "RISC-V SoC", "RISC-V chip",
        "RISC-V memory model",
        "RISC-V hypervisor", "RISC-V virtualization",
        "CHERI", "CHERI-RISC-V",
        "RISC-V verification", "RISC-V formal",
        "RISC-V vector extension", "V extension",
        "RISC-V crypto", "RISC-V scalar crypto",
        "RISC-V IOMMU", "RISC-V AIA",
        "RISC-V debug", "RISC-V trace",
        "open-source hardware",
        # RISC-V ISA Extensions
        "RV32", "RV64", "RV128",
        "RV32IMAC", "RV64GC", "RV64IMAFDC",
        "M-extension", "A-extension",
        "F-extension", "D-extension",
        "B-extension", "Bitmanip",
        "P-extension", "Packed SIMD",
        "V-extension", "Vector 1.0", "RVV 1.0",
        "H-extension", "Hypervisor extension",
        "S-extension", "Supervisor",
        "Zicsr", "Zifencei",
        "Zfh", "Zfinx",
        "Zk", "Zkr", "Zkne", "Zknd", "Zknh",
        "Sdext", "Sdtrig",
        "Smmtt", "Smstateen",
        "Svpbmt", "Svinval", "Svadu",
        "Zicond", "Zcb", "Zcmp", "Zcmt",
        "Zimop", "Zcmop",
        "RISC-V matrix", "RVV matrix", "AME",
        "matrix extension", "RISC-V AME",
        "vector length agnostic", "VLA",
        "VLEN", "DLEN", "SLEN",
        "CSR", "control status register",
        "privileged architecture", "machine mode",
        "supervisor mode", "user mode",
        "RISC-V PMP", "PMA",
        "RISC-V external debug", "RISC-V trace",
        "RISC-V interrupt", "PLIC", "CLIC",
    ]

    @property
    def conference_keywords(self) -> list:
        return [
            "architecture", "processor", "memory system",
            "cache", "pipeline", "superscalar",
            "branch prediction", "prefetch", "interconnect",
            "NoC", "network-on-chip", "multicore",
            "GPU", "accelerator", "FPGA", "ASIC",
            "RISC-V", "ISA", "instruction set",
            "DRAM", "SRAM", "NVM", "non-volatile",
            "CXL", "PCIe", "NVLink", "chiplet",
            "systolic", "tensor core", "TPU", "NPU",
            "SIMD", "SIMT", "vector", "VLIW",
            "out-of-order", "speculative",
            "power", "energy", "thermal",
            "reliability", "fault", "secure",
            "virtual memory", "TLB", "page table",
            "memory hierarchy", "near-data",
            "processing-in-memory", "PIM",
            "quantum", "neuromorphic",
            "approximate computing",
            "persistent memory", "RDMA",
            # RISC-V
            "RISC-V", "riscv", "risc-v",
            "RISC-V processor", "RISC-V core",
            "RISC-V vector", "RVV",
            "RISC-V custom", "custom instruction",
            "RISC-V ISA", "ISA extension",
            "XiangShan", "xiangshan", "香山",
            "BOOM", "SonicBOOM", "Rocket",
            "RISC-V SoC", "RISC-V chip",
            "Spike", "RISC-V simulator",
            "RISC-V memory model",
            "RISC-V hypervisor", "RISC-V virtualization",
            "CHERI", "CHERI-RISC-V",
            "RISC-V verification",
            "RISC-V vector extension", "V extension",
            "RISC-V crypto", "RISC-V scalar crypto",
            "RISC-V IOMMU", "RISC-V AIA",
            "RISC-V debug", "RISC-V trace",
            "open-source hardware",
            # RISC-V ISA Extensions
            "RV32", "RV64",
            "M-extension", "A-extension",
            "F-extension", "D-extension",
            "B-extension", "bitmanip",
            "P-extension", "packed SIMD",
            "V-extension", "vector 1.0", "RVV 1.0",
            "H-extension", "hypervisor extension",
            "Zicsr", "Zifencei",
            "Zfh", "Zfinx",
            "Sdext", "Sdtrig",
            "RISC-V matrix", "matrix extension",
            "AME", "RISC-V AME",
            "vector length agnostic", "VLA",
            "VLEN", "DLEN", "SLEN",
            "CSR", "control status register",
            "privileged architecture",
            "machine mode", "supervisor mode",
            "RISC-V PMP", "PMA",
            "RISC-V interrupt", "PLIC", "CLIC",
        ]


def main():
    bot = ArchBot()
    try:
        papers = bot.run()
        logger.info("Architecture Bot: %d papers", len(papers))
    except Exception as exc:
        logger.error("Architecture Bot failed: %s", exc)
        raise


if __name__ == "__main__":
    main()
