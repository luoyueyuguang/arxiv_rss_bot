import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_build_py_contains_cli_modules_and_excludes_tests(tmp_path):
    build_dir = tmp_path / "package"

    result = subprocess.run(
        [
            sys.executable,
            "setup.py",
            "build_py",
            "--build-lib",
            str(build_dir),
        ],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert (build_dir / "arxiv_bot.py").is_file()
    assert (build_dir / "base_conference_bot.py").is_file()
    assert (build_dir / "run_all_bots.py").is_file()
    assert (build_dir / "bots/iclr_bot.py").is_file()
    assert not (build_dir / "tests").exists()


def test_repository_contains_declared_license():
    setup = (PROJECT_ROOT / "setup.py").read_text(encoding="utf-8")
    license_text = (PROJECT_ROOT / "LICENSE").read_text(encoding="utf-8")

    assert 'license="MIT"' in setup
    assert license_text.startswith("MIT License")
