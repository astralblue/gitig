#!/usr/bin/env python3
"""Script to convert CHANGELOG.md to docs/changelog.rst using m2r2."""

import sys
from pathlib import Path

import m2r2


def find_repo_root():
    """Find the repository root by looking for pyproject.toml."""
    current = Path(__file__).parent.absolute()
    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent
    raise FileNotFoundError("Could not find repository root (pyproject.toml not found)")


def convert_changelog():
    """Convert CHANGELOG.md to docs/changelog.rst."""
    repo_root = find_repo_root()
    changelog_md = repo_root / "CHANGELOG.md"
    changelog_rst = repo_root / "docs" / "changelog.rst"

    if not changelog_md.exists():
        print(f"Error: {changelog_md} does not exist", file=sys.stderr)
        return 1

    # Read the markdown file
    with changelog_md.open("r", encoding="utf-8") as f:
        markdown_content = f.read()

    # Convert to reStructuredText
    try:
        rst_content = m2r2.convert(markdown_content)
    except Exception as e:
        print(f"Error converting markdown to rst: {e}", file=sys.stderr)
        return 1

    # Write the reStructuredText file
    with changelog_rst.open("w", encoding="utf-8") as f:
        f.write(rst_content)

    print(f"Successfully converted {changelog_md} to {changelog_rst}")
    return 0


if __name__ == "__main__":
    sys.exit(convert_changelog())
