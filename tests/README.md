# Test Suite

The default suite is deterministic and does not access arXiv, OpenReview, RSS
deployments, or model APIs.

## Setup

```bash
python3 -m pip install -r requirements-dev.txt
```

## Default Offline Suite

```bash
pytest
```

The default selection is configured in `pytest.ini` as:

```text
not integration and not rss
```

## Targeted Runs

```bash
pytest tests/core/test_bot.py
pytest tests/core/test_summary_cache.py
pytest --cov=arxiv_bot --cov=base_conference_bot --cov=run_all_bots
```

Tests marked `integration` require external network access and, for AI tests,
the relevant API credentials. Run them explicitly:

```bash
pytest -m integration
```

The optional RSS service is excluded from the default suite because it is not
currently deployed. Its legacy diagnostics remain under `tests/services/` and
are not part of the pytest quality gate. After starting the service locally,
they can be run manually with:

```bash
python3 tests/services/test_rss_service.py
```
