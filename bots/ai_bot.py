#!/usr/bin/env python3
"""
AI / AI for Science Conference Bot
Covers: ICML, NeurIPS, AAAI, IJCAI + AI4Science papers
Primary: OpenReview (for actual conference submissions)
Secondary: arXiv cs.AI, cs.LG, cs.CL, cs.CV (for preprints + AI4Science)
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


class AIBot(BaseConferenceBot):
    NAME = "ai"
    CONFERENCE_NAME = "AI / AI for Science"
    OUTPUT_DIR = "conferences/ai"
    DAYS_BACK = 7

    ARXIV_CATEGORIES = ["cs.AI", "cs.LG"]

    OPENREVIEW_DOMAINS = [
        "ICML.cc/2026/Conference",
        "ICML.cc/2025/Conference",
        "NeurIPS.cc/2026/Conference",
        "NeurIPS.cc/2025/Conference",
        "AAAI.org/2026/Conference",
        "AAAI.org/2025/Conference",
    ]

    CONFERENCE_NAME_KEYWORDS = [
        "ICML", "International Conference on Machine Learning",
        "NeurIPS", "Neural Information Processing Systems",
        "AAAI", "Association for the Advancement of Artificial Intelligence",
        "IJCAI", "International Joint Conference on Artificial Intelligence",
        "ICLR", "International Conference on Learning Representations",
        "CVPR", "Computer Vision and Pattern Recognition",
        "ICCV", "International Conference on Computer Vision",
        "ACL", "Association for Computational Linguistics",
        "EMNLP", "Empirical Methods in Natural Language Processing",
        "AI for Science",
    ]

    HIGH_SCORE_KEYWORDS = [
        "Scientific discovery", "AI for Science",
        "Physics-informed", "PINN", "Neural operator",
        "Molecular dynamics", "Molecular simulation",
        "Protein folding", "AlphaFold", "ESMFold",
        "Drug discovery", "Docking", "Molecule generation",
        "DFT", "Density functional theory",
        "Quantum chemistry", "Schrodinger",
        "CFD", "Computational fluid dynamics",
        "Climate", "Weather", "Earth system",
        "Genomics", "Proteomics", "Single cell",
        "Crystallography", "Materials",
        "PDE", "Partial differential equation",
        "Diffusion model", "Score-based",
        "Flow matching", "Continuous normalizing",
        "Graph neural network", "GNN", "Equivariant",
        "Reinforcement learning", "Policy gradient",
        "Foundation model", "Large language model",
        "Multimodal", "Vision-language",
        "Self-supervised", "Contrastive",
        "Transformer", "Mamba", "State space",
        "In-context learning", "Chain-of-thought",
        "RLHF", "DPO", "Alignment",
        "Mixture of experts", "MoE",
        "Retrieval augmented", "RAG",
        "Quantization", "Pruning", "Distillation",
        "Scalable", "Efficient training",
    ]

    @property
    def conference_keywords(self) -> list:
        return [
            "deep learning", "neural network",
            "transformer", "attention",
            "reinforcement learning", "RL",
            "generative", "GAN", "VAE", "diffusion",
            "language model", "LLM", "NLP",
            "computer vision", "image", "video",
            "graph neural", "GNN",
            "representation learning",
            "self-supervised", "unsupervised",
            "few-shot", "zero-shot", "meta-learning",
            "optimization", "SGD", "Adam",
            "federated", "privacy", "differential privacy",
            "fairness", "bias", "interpretability",
            "robustness", "adversarial",
            "AI for Science", "scientific",
            "physics", "biology", "chemistry",
            "molecular", "protein", "drug",
            "quantum", "materials",
            "climate", "weather", "earth",
            "neural operator", "FNO", "DeepONet",
            "PINN", "physics-informed",
            "equivariant", "symmetry",
            "diffusion model", "score-based",
            "flow matching", "normalizing flow",
            "foundation model", "pretrained",
            "multimodal", "vision-language",
            "in-context", "prompt", "instruction",
            "RLHF", "alignment", "DPO",
            "quantization", "pruning", "distillation",
            "MoE", "mixture of experts",
            "retrieval augmented", "RAG",
            "chain-of-thought", "reasoning",
            "scaling", "scalable", "efficient",
            "transfer learning", "domain adaptation",
            "causal", "causality",
            "uncertainty", "calibration",
            "Bayesian", "probabilistic",
        ]


def main():
    bot = AIBot()
    try:
        papers = bot.run()
        logger.info("AI Bot: %d papers", len(papers))
    except Exception as exc:
        logger.error("AI Bot failed: %s", exc)
        raise


if __name__ == "__main__":
    main()
