#!/usr/bin/env python3
"""
HPC Conference Bot
Covers: SC, PPoPP, HPDC, ICS
Primary: arXiv cs.DC, cs.PF, cs.MS
OpenReview: PPoPP, HPDC, ICS (when available)
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


class HPCBot(BaseConferenceBot):
    NAME = "hpc"
    CONFERENCE_NAME = "High Performance Computing"
    OUTPUT_DIR = "conferences/hpc"
    DAYS_BACK = 7

    ARXIV_CATEGORIES = ["cs.DC"]

    OPENREVIEW_DOMAINS = [
        "ppopp.cc/2026",
        "ppopp.cc/2025",
        "ppopp.cc/2024",
        "HPDC/2025",
        "HPDC/2024",
        "ICS/2026",
        "ICS/2025",
        "ICS/2024",
    ]

    CONFERENCE_NAME_KEYWORDS = [
        "Supercomputing", "SC '", "SC'",
        "PPoPP", "Principles and Practice of Parallel Programming",
        "HPDC", "High Performance Distributed Computing",
        "ICS", "International Conference on Supercomputing",
        "IPDPS", "International Parallel and Distributed Processing",
        "CLUSTER", "IEEE Cluster",
    ]

    HIGH_SCORE_KEYWORDS = [
        "MPI", "CUDA", "OpenMP", "MPI+OpenMP",
        "GPU", "CUDA-aware", "NCCL", "NVSHMEM",
        "RDMA", "InfiniBand", "RoCE",
        "PGAS", "UPC++", "Co-array Fortran",
        "Domain decomposition", "Stencil",
        "Sparse matrix", "Iterative solver",
        "AMR", "Adaptive mesh",
        "Load balancing", "Task scheduling",
        "Fault tolerance", "Checkpoint/restart",
        "Energy efficiency", "Power-aware",
        "Exascale", "Petascale",
        "Heterogeneous", "Accelerator",
        "FPGA", "Reconfigurable computing",
        "I/O", "Lustre", "DAOS", "burst buffer",
        "Workflow", "Jupyter", "Container",
        "Cloud HPC", "Serverless",
        # More HPC/parallel
        "GPU-aware MPI", "CUDA-aware MPI", "MPI+CUDA",
        "one-sided communication", "RMA", "active messages",
        "partitioned communication", "non-blocking collective",
        "neighborhood collective", "topology-aware", "process mapping",
        "multi-GPU", "multi-node", "GPU Direct RDMA", "GPUDirect",
        "MPS", "MIG", "CUDA stream", "CUDA graph",
        "async compute", "overlap", "pipelining",
        "double buffering", "tiling", "blocking",
        "wavefront", "stencil computation", "halo exchange", "ghost cell",
        "particle method", "N-body", "Barnes-Hut", "fast multipole",
        "FFT", "FFTW", "cuFFT", "cuBLAS", "cuSPARSE", "CUTLASS", "TensorRT",
        "OpenCL", "SYCL", "oneAPI", "Kokkos", "RAJA",
        "HPX", "Charm++", "UPC++", "Legion", "Regent",
        "Task-based", "dataflow", "DAG scheduling",
        "async task", "futures", "continuation",
        # HPC AI
        "HPC AI", "AI for HPC",
        "surrogate model", "learned solver", "neural PDE",
        "scientific ML", "SciML", "physics-ML",
        "operator learning", "DeepONet", "FNO", "neural operator",
        "PINN", "physics-informed",
    ]

    @property
    def conference_keywords(self) -> list:
        return [
            "HPC", "high performance computing",
            "parallel", "distributed", "scalable",
            "supercomputer", "supercomputing",
            "MPI", "CUDA", "OpenMP", "OpenACC",
            "GPU", "accelerator", "heterogeneous",
            "cluster", "scheduling", "job scheduler",
            "RDMA", "InfiniBand", "network",
            "MPI collective", "allreduce",
            "PGAS", "partitioned global",
            "stencil", "sparse", "linear solver",
            "domain decomposition", "FEM",
            "checkpoint", "fault tolerance",
            "energy", "power", "performance",
            "benchmark", "profiling",
            "exascale", "petascale",
            "load balancing", "task parallelism",
            "data parallel", "model parallel",
            "tensor parallelism", "pipeline parallelism",
            "communication", "synchronization",
            "NUMA", "affinity", "topology",
            "SIMD", "vectorization", "AVX",
            "memory bandwidth", "roofline",
            "I/O", "file system", "burst buffer",
        ]


def main():
    bot = HPCBot()
    try:
        papers = bot.run()
        logger.info("HPC Bot: %d papers", len(papers))
    except Exception as exc:
        logger.error("HPC Bot failed: %s", exc)
        raise


if __name__ == "__main__":
    main()
