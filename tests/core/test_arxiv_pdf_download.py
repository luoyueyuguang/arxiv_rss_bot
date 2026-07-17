import requests

import arxiv_bot


class FakeResponse:
    headers = {"content-type": "application/pdf"}

    def __init__(self, chunks=(b"%PDF-1.7\n", b"test"), error=None):
        self.chunks = chunks
        self.error = error

    def raise_for_status(self):
        if self.error:
            raise self.error

    def iter_content(self, chunk_size):
        assert chunk_size == 8192
        return iter(self.chunks)


def test_downloads_pdf_to_requested_cache(
    monkeypatch, bot_factory, paper_factory, tmp_path
):
    requested = []

    def fake_get(url, **kwargs):
        requested.append((url, kwargs))
        return FakeResponse()

    monkeypatch.setattr(arxiv_bot.requests, "get", fake_get)
    bot = bot_factory()

    path = bot.download_arxiv_pdf(paper_factory(), output_dir=tmp_path)

    assert path == tmp_path / "2607.00001v1.pdf"
    assert path.read_bytes() == b"%PDF-1.7\ntest"
    assert requested == [
        (
            "https://arxiv.org/pdf/2607.00001v1.pdf",
            {
                "stream": True,
                "timeout": 60,
                "headers": {"User-Agent": "arxiv-rss-bot/1.0 (academic research)"},
            },
        )
    ]


def test_reuses_existing_pdf_without_network(
    monkeypatch, bot_factory, paper_factory, tmp_path
):
    existing = tmp_path / "2607.00001v1.pdf"
    existing.write_bytes(b"%PDF-cached")
    monkeypatch.setattr(
        arxiv_bot.requests,
        "get",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("network should not be called")
        ),
    )

    path = bot_factory().download_arxiv_pdf(
        paper_factory(), output_dir=tmp_path
    )

    assert path == existing
    assert path.read_bytes() == b"%PDF-cached"


def test_download_failure_returns_none(
    monkeypatch, bot_factory, paper_factory, tmp_path
):
    response = FakeResponse(error=requests.HTTPError("503"))
    monkeypatch.setattr(arxiv_bot.requests, "get", lambda *_args, **_kwargs: response)

    path = bot_factory().download_arxiv_pdf(
        paper_factory(), output_dir=tmp_path
    )

    assert path is None
    assert list(tmp_path.glob("*.pdf")) == []


def test_rejects_non_arxiv_source(monkeypatch, bot_factory, paper_factory, tmp_path):
    paper = paper_factory(paper_id="invalid")
    paper["arxiv_id"] = None
    paper["id"] = None
    paper["link"] = "https://example.com/abs/2607.00001v1"
    monkeypatch.setattr(
        arxiv_bot.requests,
        "get",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("untrusted URL must not be requested")
        ),
    )

    assert bot_factory().download_arxiv_pdf(paper, output_dir=tmp_path) is None


def test_rejects_non_pdf_response(
    monkeypatch, bot_factory, paper_factory, tmp_path
):
    response = FakeResponse()
    response.headers = {"content-type": "text/html"}
    monkeypatch.setattr(arxiv_bot.requests, "get", lambda *_args, **_kwargs: response)

    assert bot_factory().download_arxiv_pdf(
        paper_factory(), output_dir=tmp_path
    ) is None
