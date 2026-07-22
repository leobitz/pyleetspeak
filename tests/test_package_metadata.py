import re
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def test_package_version_has_one_authoritative_source() -> None:
    pyproject = (REPOSITORY_ROOT / "pyproject.toml").read_text(encoding="utf-8")
    package_init = (REPOSITORY_ROOT / "pyleetspeak" / "__init__.py").read_text(encoding="utf-8")

    package_version = re.search(r'^__version__ = "([^"]+)"$', package_init, flags=re.MULTILINE)

    assert package_version is not None
    assert 'dynamic = ["version"]' in pyproject
    assert 'version = { attr = "pyleetspeak.__version__" }' in pyproject
    assert package_version.group(1) == "0.3.9"


def test_pyproject_declares_nltk_security_floor() -> None:
    pyproject = (REPOSITORY_ROOT / "pyproject.toml").read_text(encoding="utf-8")

    assert '"nltk>=3.10.0"' in pyproject
