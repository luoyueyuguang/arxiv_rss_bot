#!/usr/bin/env python3
"""
Base Conference Bot - Shared infrastructure for fetching conference papers.

Backends (tried in order, results merged):
  1. OpenReview API - for conferences hosted on OpenReview (ICML, NeurIPS, AAAI, ICLR, EuroSys)
  2. arXiv RSS feeds  - universal fallback using cs.* categories + conference name filter
"""

from __future__ import annotations

import feedparser
import json
import logging
import os
import re
import tempfile
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from tqdm import tqdm

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

OPENREVIEW_API = os.environ.get("OPENREVIEW_API", "https://api2.openreview.net")


def _ensure_directory(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def _timestamp_ms_to_datetime(timestamp_ms: Optional[int]) -> Optional[datetime]:
    if timestamp_ms is None:
        return None
    try:
        return datetime.fromtimestamp(timestamp_ms / 1000, tz=timezone.utc)
    except Exception:
        return None


def _extract_value(field: Any) -> Any:
    if isinstance(field, dict) and "value" in field:
        return field["value"]
    return field


def _extract_numeric_rating(raw_rating: Any) -> Optional[float]:
    rating_value = _extract_value(raw_rating)
    if rating_value is None:
        return None
    if isinstance(rating_value, (int, float)):
        return float(rating_value)
    if isinstance(rating_value, str):
        match = re.match(r"^\s*([0-9]+(?:\.[0-9]+)?)", rating_value)
        if match:
            try:
                return float(match.group(1))
            except ValueError:
                return None
    return None


def _normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", title).lower().strip()


def _keyword_matches(text: str, keyword: str) -> bool:
    """Match short identifiers as tokens and longer phrases as substrings."""
    normalized = keyword.strip().lower()
    if not normalized:
        return False
    if len(normalized) <= 3 and normalized.isalnum():
        pattern = rf"(?<![a-z0-9]){re.escape(normalized)}(?![a-z0-9])"
        return re.search(pattern, text.lower()) is not None
    return normalized in text.lower()


def _atomic_write_text(path: Path, content: str) -> None:
    _ensure_directory(path)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as temp_file:
        temp_file.write(content)
        temp_path = Path(temp_file.name)
    os.replace(temp_path, path)


@dataclass
class ConferencePaper:
    forum_id: str
    paper_number: int
    title: str
    authors: List[str]
    keywords: List[str]
    abstract: str
    pdf_link: Optional[str]
    forum_link: str
    submission_date: Optional[datetime]
    conference: str
    source: str = "arxiv"
    average_rating: Optional[float] = None
    rating_count: int = 0
    ratings: List[float] = field(default_factory=list)
    score: float = 0.0
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "forum_id": self.forum_id,
            "paper_number": self.paper_number,
            "title": self.title,
            "authors": self.authors,
            "keywords": self.keywords,
            "abstract": self.abstract,
            "pdf_link": self.pdf_link,
            "forum_link": self.forum_link,
            "submission_date": self.submission_date.isoformat() if self.submission_date else None,
            "conference": self.conference,
            "source": self.source,
            "average_rating": self.average_rating,
            "rating_count": self.rating_count,
            "ratings": self.ratings,
            "score": self.score,
            "updated_at": self.updated_at.isoformat(),
        }


class BaseConferenceBot(ABC):
    """Base class for conference paper bots.

    Subclasses define:
      - conference_keywords (topic filter)
      - arxiv_categories (arXiv RSS categories to fetch)
      - conference_name_keywords (keywords that identify papers from target conferences)
      - openreview_domains (optional, for conferences on OpenReview)
    """

    NAME: str = "base"
    CONFERENCE_NAME: str = "Base Conference"
    OUTPUT_DIR: str = "conferences/base"

    OPENREVIEW_DOMAINS: List[str] = []
    ARXIV_CATEGORIES: List[str] = ["cs.AI", "cs.LG"]
    CONFERENCE_NAME_KEYWORDS: List[str] = []
    HIGH_SCORE_KEYWORDS: List[str] = []
    LOW_SCORE_KEYWORDS: List[str] = []
    DAYS_BACK: int = 90

    def __init__(
        self,
        year: Optional[int] = None,
        output_dir: Optional[Path] = None,
        max_papers: Optional[int] = None,
        display_limit: Optional[int] = None,
        session: Optional[requests.Session] = None,
        config_file: str = "config.json",
        days_back: Optional[int] = None,
    ):
        self.config_file = config_file
        self.config = self._load_config()
        conf_config = self.config.get("conferences", {}).get(self.NAME, {})

        self.year = year if year is not None else conf_config.get("year", 2026)
        self.output_dir = output_dir or Path(self.OUTPUT_DIR)
        self.max_papers = (
            max_papers
            if max_papers is not None
            else conf_config.get("max_papers", 20000)
        )
        self.display_limit = (
            display_limit
            if display_limit is not None
            else conf_config.get("display_limit", self.config.get("display_limit", 100))
        )
        self.cache_limit = conf_config.get(
            "cache_limit", max(self.display_limit, 1000)
        )
        self.fetch_ratings = conf_config.get(
            "fetch_ratings", self.config.get("fetch_ratings", True)
        )
        self.min_score = conf_config.get(
            "min_score", self.config.get("min_score", 0.0)
        )
        self.allow_empty_result = conf_config.get("allow_empty_result", False)
        self.session = session or requests.Session()
        self.session.headers.update({
            "User-Agent": "arxiv-rss-bot/1.0 (arXiv paper tracker; academic research)"
        })
        if session is None:
            retry = Retry(
                total=3,
                connect=3,
                read=3,
                backoff_factor=0.5,
                status_forcelist=(429, 500, 502, 503, 504),
                allowed_methods=frozenset({"GET"}),
                respect_retry_after_header=True,
            )
            adapter = HTTPAdapter(max_retries=retry)
            self.session.mount("https://", adapter)
        self.days_back = (
            days_back
            if days_back is not None
            else conf_config.get("days_back", self.DAYS_BACK)
        )

        self.cache_path = self.output_dir / f"{self.NAME}_cache.json"
        self.readme_path = self.output_dir / "README.md"

    @property
    @abstractmethod
    def conference_keywords(self) -> List[str]:
        """Topic keywords for filtering."""

    def _load_config(self) -> Dict[str, Any]:
        try:
            with open(self.config_file, "r") as f:
                config = json.load(f)
            logger.info("Loaded config from %s for %s", self.config_file, self.CONFERENCE_NAME)
            return config
        except (OSError, json.JSONDecodeError) as e:
            logger.warning("Config load failed: %s, using defaults", e)
            return {}

    def _get_config_keywords(self) -> List[str]:
        conf_cfg = self.config.get("conferences", {}).get(self.NAME, {})
        return conf_cfg.get("keywords", self.conference_keywords)

    def matches_criteria(self, paper: ConferencePaper) -> bool:
        text = f"{paper.title} {paper.abstract}".lower()
        keywords = self._get_config_keywords()
        if keywords:
            if not any(_keyword_matches(text, kw) for kw in keywords):
                return False
        exclude_keywords = self.config.get("exclude_keywords", [])
        if exclude_keywords:
            if any(_keyword_matches(text, kw) for kw in exclude_keywords):
                return False
        return True

    def calculate_score(self, paper: ConferencePaper) -> float:
        score = 0.0
        text = f"{paper.title} {paper.abstract}".lower()
        title_lower = paper.title.lower()
        keywords = self._get_config_keywords()
        for kw in keywords:
            if _keyword_matches(text, kw):
                score += 1.0
            if _keyword_matches(title_lower, kw):
                score += 0.5
        for kw in self.HIGH_SCORE_KEYWORDS:
            if _keyword_matches(text, kw):
                score += 10
            if _keyword_matches(title_lower, kw):
                score += 20
        for kw in self.LOW_SCORE_KEYWORDS:
            if _keyword_matches(text, kw):
                score -= 10
            if _keyword_matches(title_lower, kw):
                score -= 20
        return score

    # === arXiv Backend ===

    def _match_conference(self, text: str) -> Optional[str]:
        """Return matched conference name if paper text references target conferences, else None."""
        if not self.CONFERENCE_NAME_KEYWORDS:
            return self.ARXIV_CATEGORIES[0]
        for kw in self.CONFERENCE_NAME_KEYWORDS:
            if _keyword_matches(text, kw):
                return kw
        return None

    def fetch_papers_arxiv(self) -> List[ConferencePaper]:
        papers: List[ConferencePaper] = []
        cutoff = datetime.now(tz=timezone.utc) - timedelta(days=self.days_back)
        successful_feeds = 0

        for cat in self.ARXIV_CATEGORIES:
            try:
                url = f"https://export.arxiv.org/rss/{cat}"
                logger.info("arXiv RSS: %s", url)
                feed = feedparser.parse(url)
                if feed.bozo and not feed.entries:
                    raise RuntimeError(str(feed.bozo_exception))
                successful_feeds += 1
                for entry in feed.entries:
                    try:
                        pub_date = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
                        if pub_date < cutoff:
                            continue
                        title = entry.title.strip()
                        summary = entry.summary.strip()
                        full_text = f"{title} {summary}"
                        conf_name = self._match_conference(full_text)
                        if conf_name is None:
                            continue
                        authors = (
                            [a.name for a in entry.authors]
                            if hasattr(entry, "authors")
                            else []
                        )
                        link = entry.link
                        paper_id = link.split("/")[-1]
                        papers.append(
                            ConferencePaper(
                                forum_id=paper_id,
                                paper_number=-1,
                                title=title,
                                authors=authors,
                                keywords=[cat, conf_name],
                                abstract=summary[:800],
                                pdf_link=link.replace("/abs/", "/pdf/") + ".pdf",
                                forum_link=link,
                                submission_date=pub_date,
                                conference=conf_name,
                                source="arxiv",
                            )
                        )
                    except Exception as exc:
                        logger.debug("Skip arXiv entry: %s", exc)
                logger.info("arXiv %s: %d papers (in window)", cat, len(feed.entries))
            except Exception as exc:
                logger.warning("arXiv fetch %s: %s", cat, exc)

        if self.ARXIV_CATEGORIES and successful_feeds == 0:
            raise RuntimeError("All configured arXiv conference feeds failed")

        unique: List[ConferencePaper] = []
        seen = set()
        for p in papers:
            key = _normalize_title(p.title)
            if key not in seen:
                seen.add(key)
                unique.append(p)
        logger.info("arXiv: %d unique papers after dedup (%d raw)", len(unique), len(papers))
        return unique

    # === OpenReview Backend ===

    def _fetch_openreview_notes(
        self, domain: str
    ) -> List[Dict[str, Any]]:
        notes: List[Dict[str, Any]] = []
        page_size = 10000
        try:
            url = f"{OPENREVIEW_API}/notes"
            for offset in range(0, self.max_papers, page_size):
                params = {
                    "content.venueid": f"{domain}/Submission",
                    "domain": domain,
                    "details": "replyCount,presentation,writable",
                    "offset": offset,
                    "limit": page_size,
                }
                resp = self.session.get(url, params=params, timeout=60)
                resp.raise_for_status()
                data = resp.json()
                chunk = data.get("notes") or []
                if not chunk:
                    break
                notes.extend(chunk)
                if len(chunk) < page_size:
                    break
                if len(notes) >= self.max_papers:
                    notes = notes[: self.max_papers]
                    break
        except requests.RequestException as exc:
            logger.error("OR fetch domain=%s: %s", domain, exc)
            raise
        return notes

    def _build_paper_from_openreview(
        self, submission: Dict[str, Any], conference: str
    ) -> ConferencePaper:
        content = submission.get("content", {})
        forum_id = submission.get("forum") or submission.get("id")
        number = submission.get("number") or _extract_value(content.get("number"))
        title = _extract_value(content.get("title", "Untitled"))
        authors = _extract_value(content.get("authors", []))
        kw = _extract_value(content.get("keywords", []))
        abstract = _extract_value(content.get("abstract", "")).strip()
        pdf_link = _extract_value(content.get("pdf"))
        date = _timestamp_ms_to_datetime(submission.get("cdate"))
        forum_link = f"https://openreview.net/forum?id={forum_id}"

        return ConferencePaper(
            forum_id=forum_id,
            paper_number=number or -1,
            title=title,
            authors=authors,
            keywords=kw,
            abstract=abstract,
            pdf_link=pdf_link,
            forum_link=forum_link,
            submission_date=date,
            conference=conference,
            source="openreview",
        )

    def _fetch_ratings_batch(
        self, paper_data_list: List[Tuple[int, str]]
    ) -> Dict[str, Dict[str, Any]]:
        if not paper_data_list:
            return {}
        batch_size = 5
        results: Dict[str, Dict[str, Any]] = {}
        for i in tqdm(range(0, len(paper_data_list), batch_size), desc="Ratings"):
            batch = paper_data_list[i : i + batch_size]
            forum_ids = [fid for _, fid in batch]
            try:
                params = {"forum": forum_ids, "limit": 1000}
                resp = self.session.get(f"{OPENREVIEW_API}/notes", params=params, timeout=60)
                resp.raise_for_status()
                data = resp.json()
                reviews = data.get("notes", [])
                forum_reviews: Dict[str, List[Dict]] = {}
                for rev in reviews:
                    forum_reviews.setdefault(rev.get("forum"), []).append(rev)
                for _, fid in batch:
                    revs = forum_reviews.get(fid, [])
                    ratings = []
                    for rev in revs:
                        rv = _extract_value(rev.get("content", {}).get("rating"))
                        parsed = _extract_numeric_rating(rv)
                        if parsed is not None:
                            ratings.append(parsed)
                    results[fid] = {
                        "ratings": ratings,
                        "average": sum(ratings) / len(ratings) if ratings else None,
                    }
            except Exception as exc:
                logger.warning("Batch ratings: %s", exc)
                for _, fid in batch:
                    results[fid] = {"ratings": [], "average": None}
        return results

    def fetch_papers_openreview(self) -> List[ConferencePaper]:
        all_papers: List[ConferencePaper] = []
        successful_domains = 0
        for domain in self.OPENREVIEW_DOMAINS:
            logger.info("OpenReview: %s", domain)
            try:
                subs = self._fetch_openreview_notes(domain)
                successful_domains += 1
            except requests.RequestException:
                continue
            logger.info("  %d submissions", len(subs))
            conf = domain.split("/")[0] if "/" in domain else domain
            for sub in subs:
                try:
                    all_papers.append(self._build_paper_from_openreview(sub, conf))
                except Exception as exc:
                    logger.error("Build paper: %s", exc)
        if self.OPENREVIEW_DOMAINS and successful_domains == 0:
            logger.warning("All OpenReview domains failed; continuing without OpenReview data")
        return all_papers


    def _fetch_usenix_papers(self) -> List[ConferencePaper]:
        """Fetch papers from USENIX conference proceedings.

        Override in subclass and return a list of USENIX_URLS to enable.
        """
        return []

    DBLP_VENUES: list = []  # Override in subclass: [(conf_name, dblp_url), ...]

    def _fetch_dblp_papers(self) -> List[ConferencePaper]:
        """Fetch papers from DBLP conference proceedings (XML)."""
        if not self.DBLP_VENUES:
            return []

        try:
            from bs4 import BeautifulSoup
        except ImportError:
            logger.warning("beautifulsoup4 not installed, skipping DBLP")
            return []

        papers = []
        successful_venues = 0
        for conf_name, url in self.DBLP_VENUES:
            try:
                xml_url = url.rstrip("/") + ".xml" if not url.endswith(".xml") else url
                logger.info("DBLP: %s from %s", conf_name, xml_url)
                resp = self.session.get(xml_url, timeout=30)
                if resp.status_code != 200:
                    logger.warning("  %s returned %d", conf_name, resp.status_code)
                    continue
                successful_venues += 1

                soup = BeautifulSoup(resp.text, "xml")
                # DBLP XML: <inproceedings>, <article>, etc. with <title>, <author>, <pages>
                entries = soup.find_all(["inproceedings", "article"])
                if not entries:
                    logger.info("  %s: no entries found", conf_name)
                    continue

                conf_papers = []
                for idx, entry in enumerate(entries, 1):
                    title_el = entry.find("title")
                    if not title_el:
                        continue
                    title = title_el.get_text(strip=True)

                    authors = []
                    for author_el in entry.find_all("author"):
                        name = author_el.get_text(strip=True)
                        if name:
                            authors.append(name)

                    # DBLP often links to an open-access PDF via <ee> element
                    pdf_link = None
                    ee_el = entry.find("ee")
                    if ee_el:
                        pdf_link = ee_el.get_text(strip=True)

                    forum_link = url.removesuffix(".xml")

                    conf_papers.append(ConferencePaper(
                        forum_id=f"dblp-{re.sub(r'[^a-zA-Z0-9]', '', conf_name).lower()}-{idx}",
                        paper_number=idx,
                        title=title,
                        authors=authors if authors else ["Unknown"],
                        keywords=[],
                        abstract=f"DBLP entry. {conf_name}.",
                        pdf_link=pdf_link or forum_link,
                        forum_link=forum_link,
                        submission_date=None,
                        conference=conf_name,
                        source="dblp",
                    ))

                papers.extend(conf_papers)
                logger.info("  %s: %d papers", conf_name, len(conf_papers))
            except Exception as exc:
                logger.error("DBLP %s failed: %s", conf_name, exc)

        if self.DBLP_VENUES and successful_venues == 0:
            raise RuntimeError("All configured DBLP venues failed")
        logger.info("DBLP total: %d papers", len(papers))
        return papers
    # === Unified fetch ===

    def fetch_papers(self) -> List[ConferencePaper]:
        papers: List[ConferencePaper] = []
        failed_sources = set()
        successful_backends = 0

        # 1. arXiv (primary, works for all)
        if self.ARXIV_CATEGORIES:
            try:
                papers.extend(self.fetch_papers_arxiv())
                successful_backends += 1
            except Exception as exc:
                failed_sources.add("arxiv")
                logger.warning("arXiv backend failed: %s", exc)

        # 2. OpenReview (secondary, only for conferences that use it)
        if self.OPENREVIEW_DOMAINS:
            try:
                papers.extend(self.fetch_papers_openreview())
                successful_backends += 1
            except Exception as exc:
                failed_sources.add("openreview")
                logger.warning("OpenReview backend failed: %s", exc)

        # 3. USENIX proceedings (conference-specific)
        has_venue_backend = (
            type(self)._fetch_usenix_papers is not BaseConferenceBot._fetch_usenix_papers
        )
        if has_venue_backend:
            try:
                papers.extend(self._fetch_usenix_papers())
                successful_backends += 1
            except Exception as exc:
                failed_sources.update({"usenix", "mlr", "neurips"})
                logger.warning("Venue backend failed: %s", exc)

        # 4. DBLP proceedings (universal CS conference coverage)
        if self.DBLP_VENUES:
            try:
                papers.extend(self._fetch_dblp_papers())
                successful_backends += 1
            except Exception as exc:
                failed_sources.add("dblp")
                logger.warning("DBLP backend failed: %s", exc)

        if successful_backends == 0:
            if self.allow_empty_result:
                logger.warning("All data sources failed for %s; returning empty (allow_empty_result=True)", self.CONFERENCE_NAME)
                return []
            raise RuntimeError(f"All data sources failed for {self.CONFERENCE_NAME}")

        if failed_sources:
            fresh_keys = {(paper.source, _normalize_title(paper.title)) for paper in papers}
            for cached in self.load_papers_from_cache():
                source = cached.source
                key = (source, _normalize_title(cached.title))
                if source in failed_sources and key not in fresh_keys:
                    papers.append(cached)

        unique = self._merge_papers_by_title(papers)

        # Filter & score
        filtered = []
        for paper in unique:
            if self.matches_criteria(paper):
                paper.score = self.calculate_score(paper)
                if paper.score >= self.min_score:
                    filtered.append(paper)

        logger.info("Total: %d papers (from %d raw)", len(filtered), len(unique))

        # Fetch ratings for top OpenReview papers
        or_top = [p for p in filtered if p.source == "openreview"]
        if or_top and self.fetch_ratings:
            sorted_or = sorted(or_top, key=lambda p: p.score, reverse=True)[: self.display_limit]
            pd_list = [(i + 1, p.forum_id) for i, p in enumerate(sorted_or)]
            ratings = self._fetch_ratings_batch(pd_list)
            for i, paper in enumerate(sorted_or):
                _, fid = pd_list[i]
                info = ratings.get(fid, {"ratings": [], "average": None})
                paper.average_rating = info["average"]
                paper.rating_count = len(info["ratings"])
                paper.ratings = info["ratings"]
            rated = sum(1 for p in sorted_or if p.average_rating is not None)
            logger.info("Ratings: %d/%d OR papers", rated, len(sorted_or))

        filtered.sort(key=lambda paper: paper.score, reverse=True)
        return filtered[: self.cache_limit]

    @staticmethod
    def _merge_papers_by_title(
        papers: Iterable[ConferencePaper],
    ) -> List[ConferencePaper]:
        source_priority = {
            "openreview": 50,
            "usenix": 45,
            "mlr": 45,
            "neurips": 45,
            "dblp": 30,
            "arxiv": 10,
        }
        grouped: Dict[str, List[ConferencePaper]] = {}
        for paper in papers:
            grouped.setdefault(_normalize_title(paper.title), []).append(paper)

        merged: List[ConferencePaper] = []
        for candidates in grouped.values():
            candidates.sort(
                key=lambda paper: source_priority.get(paper.source, 20),
                reverse=True,
            )
            preferred = candidates[0]
            for fallback in candidates[1:]:
                if not preferred.abstract and fallback.abstract:
                    preferred.abstract = fallback.abstract
                if not preferred.authors and fallback.authors:
                    preferred.authors = fallback.authors
                if not preferred.pdf_link and fallback.pdf_link:
                    preferred.pdf_link = fallback.pdf_link
                if not preferred.submission_date and fallback.submission_date:
                    preferred.submission_date = fallback.submission_date
                preferred.keywords = list(
                    dict.fromkeys(preferred.keywords + fallback.keywords)
                )
            merged.append(preferred)
        return merged

    # === Caching ===

    def save_cache(self, papers: Iterable[ConferencePaper]) -> None:
        plist = [p.to_dict() for p in papers]
        cached_by_key = {
            self._cache_record_key(record): record
            for record in self.load_cached_papers()
        }
        for record in plist:
            cached = cached_by_key.get(self._cache_record_key(record))
            if cached and self._same_cached_content(cached, record):
                record["updated_at"] = cached.get("updated_at", record["updated_at"])

        payload = {
            "name": self.NAME,
            "conference": self.CONFERENCE_NAME,
            "last_updated": datetime.now(timezone.utc).isoformat(),
            "paper_count": len(plist),
            "papers": plist,
        }
        _atomic_write_text(
            self.cache_path,
            json.dumps(payload, indent=2, ensure_ascii=False),
        )
        logger.info("Saved %d papers to %s", len(plist), self.cache_path)

    @staticmethod
    def _cache_record_key(record: Dict[str, Any]) -> Tuple[str, str]:
        return (
            str(record.get("source", "")),
            str(record.get("forum_id") or _normalize_title(record.get("title", ""))),
        )

    @staticmethod
    def _same_cached_content(
        old_record: Dict[str, Any], new_record: Dict[str, Any]
    ) -> bool:
        ignored = {"updated_at"}
        return {
            key: value for key, value in old_record.items() if key not in ignored
        } == {
            key: value for key, value in new_record.items() if key not in ignored
        }

    def load_cached_papers(self) -> List[Dict[str, Any]]:
        if not self.cache_path.exists():
            return []
        try:
            with self.cache_path.open("r", encoding="utf-8") as f:
                return json.load(f).get("papers", [])
        except (json.JSONDecodeError, OSError) as exc:
            logger.warning("Load cache: %s", exc)
            return []

    def load_papers_from_cache(self) -> List[ConferencePaper]:
        raw = self.load_cached_papers()
        papers = []
        for d in raw:
            try:
                papers.append(ConferencePaper(
                    forum_id=d.get("forum_id", ""),
                    paper_number=d.get("paper_number", -1),
                    title=d.get("title", ""),
                    authors=d.get("authors", []),
                    keywords=d.get("keywords", []),
                    abstract=d.get("abstract", ""),
                    pdf_link=d.get("pdf_link"),
                    forum_link=d.get("forum_link", ""),
                    submission_date=datetime.fromisoformat(d["submission_date"]) if d.get("submission_date") else None,
                    conference=d.get("conference", ""),
                    source=d.get("source", "arxiv"),
                    average_rating=d.get("average_rating"),
                    rating_count=d.get("rating_count", 0),
                    ratings=d.get("ratings", []),
                    score=d.get("score", 0.0),
                    updated_at=datetime.fromisoformat(d["updated_at"])
                    if d.get("updated_at")
                    else datetime.now(timezone.utc),
                ))
            except Exception:
                continue
        logger.info("Loaded %d papers from cache (skipping fetch)", len(papers))
        return papers

    # === Rendering ===

    def render_readme(self, papers: List[ConferencePaper]) -> str:
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        total = len(papers)
        sorted_papers = sorted(papers, key=lambda p: p.score, reverse=True)
        display = sorted_papers[: self.display_limit]
        rated = sum(1 for p in papers if p.average_rating is not None)
        source_counts: Dict[str, int] = {}
        for paper in display:
            source_counts[paper.source] = source_counts.get(paper.source, 0) + 1
        source_summary = ", ".join(
            f"{source}: {count}" for source, count in sorted(source_counts.items())
        )

        lines = [
            f"# {self.CONFERENCE_NAME} Papers",
            "",
            f"- **Last Updated**: {ts}",
            f"- **Total Filtered Papers**: {total}",
            f"- **Displaying**: {len(display)} ({source_summary or 'no sources'})",
            f"- **Papers with Ratings**: {rated}",
            f"- **Lookback**: {self.days_back} days",
            "",
            "",
        ]
        if not display:
            lines.append("> No papers matched the current keyword filters.")
            return "\n".join(lines)

        has_ratings = any(p.average_rating is not None for p in display)
        if has_ratings:
            header = "| # | Title | Source | Ratings | Avg | Reviews |\n"
            divider = "| --- | --- | --- | --- | --- | --- |\n"
        else:
            header = "| # | Title | Source | Score |\n"
            divider = "| --- | --- | --- | --- |\n"

        rows: List[str] = []
        for idx, paper in enumerate(display, 1):
            title = paper.title.replace("\n", " ").replace("|", "\\|").strip()
            source_tag = f"`{paper.source.upper()}`"
            if has_ratings:
                avg = f"{paper.average_rating:.2f}" if paper.average_rating else "N/A"
                revs = str(paper.rating_count) if paper.rating_count else "0"
                rates = ",".join(str(round(r)) for r in paper.ratings) if paper.ratings else "N/A"
                rows.append(
                    f"| {idx} | [{title}]({paper.forum_link}) | {source_tag} | **{rates}** | **{avg}** | {revs} |"
                )
            else:
                rows.append(
                    f"| {idx} | [{title}]({paper.forum_link}) | {source_tag} | {paper.score:.1f} |"
                )

        return "\n".join(lines + [header + divider + "\n".join(rows)])

    def update_readme(self, papers: List[ConferencePaper]) -> None:
        content = self.render_readme(papers)
        _atomic_write_text(self.readme_path, content)
        logger.info("Updated %s", self.readme_path)

    def run(self) -> List[ConferencePaper]:
        logger.info("=== Running %s Bot ===", self.CONFERENCE_NAME)
        papers = self.fetch_papers()
        if not papers and not self.allow_empty_result:
            cached_count = len(self.load_cached_papers())
            raise RuntimeError(
                f"{self.CONFERENCE_NAME} produced no papers; "
                f"preserved {cached_count} cached records"
            )
        self.save_cache(papers)
        self.update_readme(papers)
        logger.info("%s Bot done: %d papers", self.CONFERENCE_NAME, len(papers))
        return papers
