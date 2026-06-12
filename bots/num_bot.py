#!/usr/bin/env python3
"""
Numerical Analysis / Scientific Computing Conference Bot
Covers: SIAM, ICIAM, related numerical conferences
Primary: arXiv cs.NA, math.NA, cs.CE, physics.comp-ph
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


class NumBot(BaseConferenceBot):
    NAME = "num"
    CONFERENCE_NAME = "Numerical Analysis / Scientific Computing"
    OUTPUT_DIR = "conferences/num"
    DAYS_BACK = 7

    ARXIV_CATEGORIES = ["cs.NA"]

    CONFERENCE_NAME_KEYWORDS = [
        "SIAM", "Society for Industrial and Applied Mathematics",
        "ICIAM", "International Congress on Industrial and Applied Mathematics",
        "NA", "numerical analysis",
        "scientific computing",
    ]

    HIGH_SCORE_KEYWORDS = [
        "Finite element", "Multigrid", "AMG",
        "Discontinuous Galerkin", "Spectral element",
        "Domain decomposition", "Preconditioner",
        "Krylov subspace", "GMRES",
        "hp-adaptivity", "Isogeometric",
        "Computational fluid dynamics",
        "Navier-Stokes", "Turbulence",
        "Uncertainty quantification",
        "Model order reduction", "POD",
        "Fast multipole method", "FMM",
        "PETSc", "Trilinos", "deal.II", "FEniCS",
    ]

    @property
    def conference_keywords(self) -> list:
        return [
            "numerical", "numerical method",
            "finite element", "FEM", "finite difference",
            "finite volume", "spectral method",
            "discontinuous Galerkin", "DG",
            "multigrid", "AMG", "preconditioner",
            "iterative solver", "Krylov", "GMRES", "CG",
            "sparse matrix", "sparse linear algebra",
            "eigenvalue", "SVD", "factorization",
            "time integration", "ODE", "PDE",
            "partial differential equation",
            "computational fluid dynamics", "CFD",
            "computational mechanics",
            "structural analysis", "solid mechanics",
            "electromagnetics", "Maxwell",
            "acoustics", "wave propagation",
            "porous media", "Darcy", "Stokes",
            "adaptive mesh", "AMR", "hp-adaptivity",
            "uncertainty quantification", "UQ",
            "stochastic", "Monte Carlo",
            "optimization", "PDE-constrained",
            "adjoint", "sensitivity",
            "model order reduction", "POD", "reduced basis",
            "scientific computing",
            "high-order", "spectral element",
            "isogeometric analysis", "IGA",
            "mesh generation", "mesh quality",
            "parallel computing", "domain decomposition",
            "GPU", "CUDA", "accelerator",
            "linear solver", "direct solver",
            "preconditioning", "Krylov subspace",
            "Navier-Stokes", "turbulence",
            "aeroacoustics", "compressible",
            "incompressible", "multiphase",
            "fluid-structure interaction",
            "lattice Boltzmann", "LBM",
            "molecular dynamics", "MD",
            "density functional theory", "DFT",
            "quantum", "electronic structure",
            "fast multipole", "FMM",
            "boundary element", "BEM",
            "integral equation",
            "singular", "near-singular",
            "octree", "quadtree", "kd-tree",
            "dense linear algebra",
            "BLAS", "LAPACK", "ScaLAPACK",
            "Eigen", "PETSc", "Trilinos",
            "deal.II", "FEniCS", "MFEM",
            "open source", "software",
        ]


def main():
    bot = NumBot()
    try:
        papers = bot.run()
        logger.info("Numerical Bot: %d papers", len(papers))
    except Exception as exc:
        logger.error("Numerical Bot failed: %s", exc)
        raise


if __name__ == "__main__":
    main()
