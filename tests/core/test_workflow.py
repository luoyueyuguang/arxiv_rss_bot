import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_repository_config_has_required_shape():
    config = json.loads((PROJECT_ROOT / "config.json").read_text(encoding="utf-8"))

    assert config["categories"]
    assert config["keywords"]
    assert config["max_papers"] > 0
    assert config["days_back"] > 0
    assert config["min_score"] >= 0
    assert set(config["conferences"]) >= {
        "arch",
        "hpc",
        "sys",
        "chip",
        "ai",
        "num",
        "iclr",
    }


def test_readme_template_contains_all_runtime_placeholders():
    template = (PROJECT_ROOT / "README.template.md").read_text(encoding="utf-8")

    assert {
        "{{LAST_UPDATED}}",
        "{{PAPER_COUNT}}",
        "{{CATEGORIES}}",
        "{{KEYWORDS}}",
        "{{PAPERS_SECTION}}",
    } <= set(part for part in template.split() if part.startswith("{{"))


def test_core_workflows_run_pytest_before_generators():
    workflow_paths = [
        PROJECT_ROOT / ".github/workflows/arxiv_bot.yml",
        PROJECT_ROOT / ".github/workflows/update-conferences.yml",
    ]

    for workflow_path in workflow_paths:
        workflow = workflow_path.read_text(encoding="utf-8")
        expected_generator = (
            "python arxiv_bot.py"
            if workflow_path.name == "arxiv_bot.yml"
            else "python run_all_bots.py"
        )
        assert "pip install -r requirements-dev.txt" in workflow
        assert "pytest" in workflow
        assert workflow.index("pytest") < workflow.index(expected_generator)
        assert "tests/**" in workflow
        assert 'python-version: "3.12"' in workflow or "python-version: '3.12'" in workflow
        assert "paper-updates-${{ github.ref }}" in workflow
        assert 'origin "${GITHUB_REF_NAME}"' in workflow
        assert 'HEAD:${GITHUB_REF_NAME}' in workflow
