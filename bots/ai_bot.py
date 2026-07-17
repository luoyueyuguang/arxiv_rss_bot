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
import re

import logging
from base_conference_bot import BaseConferenceBot, ConferencePaper

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
    # Venue proceedings to scrape
    MLR_URLS: list = [
        ("ICML '25", "https://proceedings.mlr.press/v274/"),
    ]
    NEURIPS_URL = "https://proceedings.neurips.cc/paper_files/paper/2025"

    def _fetch_usenix_papers(self) -> list:
        """Fetch papers from MLR Press and NeurIPS proceedings."""
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            logger.warning("beautifulsoup4 not installed, skipping MLR")
            return []

        papers = []
        for conf_name, url in self.MLR_URLS:
            try:
                logger.info("MLR: %s from %s", conf_name, url)
                resp = self.session.get(url, timeout=30)
                if resp.status_code != 200:
                    logger.warning("  %s returned %d, skipping", conf_name, resp.status_code)
                    continue
                soup = BeautifulSoup(resp.text, "lxml")

                paper_divs = soup.select("div.paper")
                if not paper_divs:
                    logger.info("  %s: no papers found", conf_name)
                    continue

                conf_papers = []
                for paper_div in paper_divs:
                    title_el = paper_div.select_one("p.title")
                    if not title_el:
                        continue
                    title = title_el.get_text(strip=True)

                    authors_el = paper_div.select_one("span.authors")
                    authors_text = authors_el.get_text(strip=True) if authors_el else ""
                    authors = [a.strip() for a in authors_text.split(",") if a.strip()]

                    # Get info line for pages/venue
                    info_el = paper_div.select_one("span.info")
                    info_text = info_el.get_text(strip=True) if info_el else ""

                    # Get abs link for abstract and PDF
                    abs_link = None
                    pdf_link = None
                    links_el = paper_div.select_one("p.links")
                    if links_el:
                        for a in links_el.select("a"):
                            href = a.get("href", "")
                            text = a.get_text(strip=True)
                            if text == "abs" and href:
                                abs_link = href if href.startswith("http") else f"https://proceedings.mlr.press{href}" if href.startswith("/") else f"{url}{href}"
                            elif "Download PDF" in text and href:
                                pdf_link = href

                    if not title or not authors:
                        continue

                    # Fetch abstract from paper page (rate-limited: 0.5s delay)
                    abstract = ""
                    if abs_link:
                        try:
                            import time
                            time.sleep(0.5)  # Be respectful to MLR Press
                            abs_resp = self.session.get(abs_link, timeout=15)
                            if abs_resp.status_code == 429:
                                logger.warning("  MLR rate limited, waiting 5s...")
                                time.sleep(5)
                                abs_resp = self.session.get(abs_link, timeout=15)
                            abs_soup = BeautifulSoup(abs_resp.text, "lxml")
                            abstract_el = abs_soup.select_one("meta[property='og:description']")
                            if abstract_el:
                                abstract = abstract_el.get("content", "")
                        except Exception:
                            pass
                    clean_name = re.sub(r"[^a-zA-Z0-9]", "", conf_name).lower()
                    forum_id = f"mlr-{clean_name}-{len(conf_papers)+1}"
                    conf_papers.append(ConferencePaper(
                        forum_id=forum_id,
                        paper_number=len(conf_papers) + 1,
                        title=title,
                        authors=authors if authors else ["Unknown"],
                        keywords=[],
                        abstract=abstract[:2000] if abstract else info_text[:500],
                        pdf_link=pdf_link or abs_link or url,
                        forum_link=abs_link or url,
                        submission_date=None,
                        conference=conf_name,
                        source="mlr",
                    ))

                papers.extend(conf_papers)
                logger.info("  %s: %d papers", conf_name, len(conf_papers))
            except Exception as exc:
                logger.error("MLR %s failed: %s", conf_name, exc)


        # --- NeurIPS proceedings ---
        if self.NEURIPS_URL:
            try:
                logger.info("NeurIPS: from %s", self.NEURIPS_URL)
                resp = self.session.get(self.NEURIPS_URL, timeout=30)
                if resp.status_code == 200:
                    soup = BeautifulSoup(resp.text, "lxml")
                    # Papers are in <li> elements with links to abstract pages
                    paper_links = soup.select("a[href*='-Abstract-Conference.html']")
                    if not paper_links:
                        paper_links = soup.select("a[href*='-Abstract-Datasets_and_Benchmarks_Track.html']")
                    conf_papers = []
                    seen_titles = set()
                    for link in paper_links:
                        title = link.get_text(strip=True)
                        href = link.get("href", "")
                        if not title or title in seen_titles:
                            continue
                        seen_titles.add(title)
                        forum_link = f"https://proceedings.neurips.cc{href}" if href.startswith("/") else href
                        # Authors: text nodes after the link before the next tag
                        parent = link.parent
                        authors_text = ""
                        if parent:
                            full_text = parent.get_text(" ", strip=True)
                            # Remove the title from the beginning
                            if full_text.startswith(title):
                                authors_text = full_text[len(title):].strip()
                        authors = [a.strip() for a in authors_text.split(",") if a.strip() and len(a.strip()) > 1]

                        conf_papers.append(ConferencePaper(
                            forum_id=f"neurips25-{len(conf_papers)+1}",
                            paper_number=len(conf_papers) + 1,
                            title=title,
                            authors=authors[:10] if authors else ["Unknown"],
                            keywords=[],
                            abstract="",
                            pdf_link=forum_link,
                            forum_link=forum_link,
                            submission_date=None,
                            conference="NeurIPS '25",
                            source="neurips",
                        ))

                    papers.extend(conf_papers)
                    logger.info("  NeurIPS '25: %d papers", len(conf_papers))
                else:
                    logger.warning("  NeurIPS returned %d", resp.status_code)
            except Exception as exc:
                logger.error("NeurIPS failed: %s", exc)

        logger.info("Venue total: %d papers", len(papers))
        return papers

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
