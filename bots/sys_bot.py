#!/usr/bin/env python3
"""
Systems Conference Bot
Covers: OSDI, SOSP, EuroSys, USENIX ATC, NSDI, FAST, ASPLOS, MLSys,
        AI Infra, AI Compiler, RISC-V
Primary: arXiv cs.OS, cs.DC
OpenReview: EuroSys, MLSys (when available)
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


class SysBot(BaseConferenceBot):
    NAME = "sys"
    CONFERENCE_NAME = "Systems / AI Infra / AI Compiler / RISC-V"
    OUTPUT_DIR = "conferences/sys"
    DAYS_BACK = 7

    ARXIV_CATEGORIES = ["cs.OS", "cs.DC"]

    OPENREVIEW_DOMAINS = [
        "EuroSys/2026",
        "EuroSys/2025",
        "EuroSys/2024",
        "MLSys/2026",
        "MLSys/2025",
        "MLSys/2024",
    ]

    CONFERENCE_NAME_KEYWORDS = [
        "OSDI", "Operating Systems Design and Implementation",
        "SOSP", "Symposium on Operating Systems Principles",
        "EuroSys", "European Conference on Computer Systems",
        "USENIX ATC", "USENIX Annual Technical Conference",
        "NSDI", "Networked Systems Design and Implementation",
        "FAST", "File and Storage Technologies",
        "ASPLOS", "Architectural Support for Programming Languages and Operating Systems",
        "MLSys", "Machine Learning and Systems",
        "VEE", "Virtual Execution Environments",
        "APSys", "Asia-Pacific Workshop on Systems",
        "HotOS", "Hot Topics in Operating Systems",
        "SoCC", "Symposium on Cloud Computing",
        "CGO", "Code Generation and Optimization",
        "PLDI", "Programming Language Design and Implementation",
        "OOPSLA", "Object-Oriented Programming Systems Languages",
        "CARRV", "Computer Architecture Research with RISC-V",
        "RISC-V Summit", "RISC-V International",
    ]

    HIGH_SCORE_KEYWORDS = [
        # System
        "Operating system", "Kernel", "Linux",
        "Virtualization", "Hypervisor", "Container",
        "File system", "FS", "ext4", "ZFS", "Btrfs",
        "Key-value store", "LSM-tree", "RocksDB",
        "Consensus", "Paxos", "Raft", "BFT",
        "Distributed transaction", "2PC", "Spanner",
        "Geo-distributed", "WAN", "Byzantine",
        "Disaggregated", "Disaggregation",
        "Memory management", "Garbage collection",
        "Microkernel", "unikernel", "seL4",
        "eBPF", "XDP", "DPDK", "RDMA",
        "Persistent memory", "Optane", "PMEM",
        "Crash consistency", "Journaling",
        "Fuzzing", "Symbolic execution",
        "Verification", "Formal",
        "Remote memory", "Far memory",
        "Serverless", "FaaS",
        "RDMA", "NVMe-oF",
        # AI Infra / MLSys
        "LLM serving", "Inference serving",
        "Model serving", "Serving system",
        "Distributed training", "Training system",
        "GPU cluster", "GPU scheduling",
        "AI compiler", "TVM", "XLA", "Triton",
        "CUDA kernel", "Kernel fusion",
        "Pipeline parallelism", "Tensor parallelism",
        "Expert parallelism", "Sequence parallelism",
        "FlashAttention", "PagedAttention",
        "Continuous batching", "Dynamic batching",
        "KV cache", "KV cache management",
        "Speculative decoding", "Speculative inference",
        "Model quantization", "Weight quantization",
        "LoRA", "QLoRA", "Fine-tuning system",
        "Mixture of experts", "MoE serving",
        "vLLM", "SGLang", "TensorRT-LLM",
        "DeepSpeed", "Megatron-LM", "FSDP",
        "Ray", "Kubernetes", "GPU operator",
        "ML compiler", "MLIR",
        # AI Compiler
        "torch.compile", "TorchInductor", "TorchDynamo",
        "TACO", "Tensor algebra compiler",
        "Halide", "Halide language",
        "Polyhedral compilation", "Polyhedral model",
        "Auto-scheduler", "Auto-tuning", "AutoTVM", "Ansor",
        "Graph optimization", "Graph-level optimization",
        "Operator fusion", "Horizontal fusion", "Vertical fusion",
        "Loop tiling", "Loop unrolling", "Loop permutation",
        "Loop transformation", "Loop nest optimization",
        "Code generation", "CodeGen",
        "Intermediate representation", "IR lowering",
        "Buffer scheduling", "Memory planning", "Memory reuse",
        "Tile", "Tiled execution",
        "Roller", "Rammer", "Welder", "DietCode",
        "TensorIR", "Relay", "TE",
        "PTX", "SPIR-V", "GPU code generation",
        # RISC-V
        "RISC-V", "RISC-V processor",
        "RISC-V vector", "RVV", "Vector extension",
        "RISC-V custom", "Custom instruction",
        "RISC-V ISA", "ISA extension",
        "XiangShan", "Xiangshan",
        "BOOM", "SonicBOOM", "Rocket chip",
        "Spike simulator", "RISC-V simulator",
        "RISC-V core", "RISC-V SoC",
        "RISC-V memory model",
        "RISC-V hypervisor", "RISC-V virtualization",
        "CHERI", "CHERI-RISC-V",
        "RISC-V verification", "RISC-V formal",
    ]

    @property
    def conference_keywords(self) -> list:
        return [
            # Systems
            "operating system", "kernel", "file system",
            "virtualization", "container", "hypervisor",
            "distributed system", "consensus", "fault tolerance",
            "storage", "database", "key-value",
            "transaction", "replication", "consistency",
            "disaggregated", "RDMA", "persistent memory",
            "crash", "recovery",
            "memory management", "garbage collection",
            "microkernel", "unikernel",
            "eBPF", "XDP", "DPDK",
            "verification", "formal methods",
            "bug", "fuzzing", "testing",
            "isolation", "sandbox", "TEE",
            "serverless", "FaaS", "cloud",
            "scheduling", "resource",
            "networking", "TCP", "congestion",
            "software-defined", "NFV",
            "Linux", "compiler", "LLVM", "JIT",
            "runtime", "library OS",
            "sharding", "partitioning",
            "caching", "cache coherence",
            "NVM", "SSD", "flash",
            # AI Infra / MLSys
            "LLM serving", "model serving",
            "inference serving", "inference system",
            "distributed training", "training system",
            "deep learning system", "machine learning system",
            "GPU cluster", "GPU scheduling", "GPU memory",
            "AI compiler", "TVM", "XLA", "Triton",
            "CUDA kernel", "kernel launch",
            "pipeline parallelism", "tensor parallelism",
            "data parallelism", "model parallelism",
            "FlashAttention", "PagedAttention",
            "continuous batching", "batching",
            "KV cache", "kv cache",
            "speculative decoding", "speculative inference",
            "quantization", "model quantization",
            "LoRA", "fine-tuning", "finetuning",
            "mixture of experts", "MoE",
            "vLLM", "SGLang", "TensorRT",
            "DeepSpeed", "Megatron", "FSDP",
            "Ray", "Kubernetes",
            "ML compiler", "MLIR",
            "offloading", "offload",
            "prefill", "decode", "decoding",
            "token generation", "throughput",
            "latency", "service level",
            "model parallelism", "expert parallelism",
            "collective communication", "allreduce",
            "gradient compression", "gradient",
            "checkpoint", "checkpointing",
            "fault tolerance", "elastic",
            "heterogeneous", "accelerator",
            "NPU", "TPU", "GPU",
            # AI Compiler
            "torch.compile", "inductor",
            "TACO", "tensor algebra",
            "Halide",
            "polyhedral", "polyhedral compilation",
            "auto-scheduler", "auto-tuning", "autotvm", "ansor",
            "graph optimization", "operator fusion",
            "kernel fusion", "kernel compilation",
            "loop tiling", "loop unrolling", "loop permutation",
            "loop transformation", "loop optimization",
            "code generation", "codegen",
            "intermediate representation", "IR",
            "IR lowering", "IR design",
            "buffer scheduling", "memory planning",
            "tensor program", "tensor expression",
            "PTX", "SPIR-V", "GPU code generation",
            "compile time", "just-in-time", "ahead-of-time",
            "dynamic shape", "static shape",
            "symbolic shape", "shape inference",
            "layout optimization", "data layout",
            "memory hierarchy", "memory reuse",
            "vectorization", "SIMD", "SIMT",
            # RISC-V
            "RISC-V", "riscv", "risc-v",
            "RISC-V vector", "RVV",
            "RISC-V custom", "custom instruction",
            "RISC-V ISA", "ISA extension",
            "XiangShan", "xiangshan", "香山",
            "BOOM", "SonicBOOM", "Rocket",
            "RISC-V core", "RISC-V processor", "RISC-V SoC",
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
        ]


def main():
    bot = SysBot()
    try:
        papers = bot.run()
        logger.info("Systems Bot: %d papers", len(papers))
    except Exception as exc:
        logger.error("Systems Bot failed: %s", exc)
        raise


if __name__ == "__main__":
    main()
