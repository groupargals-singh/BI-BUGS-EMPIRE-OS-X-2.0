#!/usr/bin/env python3
"""Read-only, backward-compatible lifecycle-header audit for BI-BUGS specs."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_DIR = ROOT / "docs" / "MASTER_SPECIFICATION"
DIMENSIONS = {
    "Specification status": ("Specification status", "Status"),
    "Implementation status": ("Implementation status", "Implementation"),
    "Testing status": ("Testing status", "Testing"),
    "Production status": ("Production status", "Production"),
}
FIELD_RE = re.compile(r"^\s*\*\*(?P<label>[^*]+):\*\*\s*(?P<value>.*?)\s*$")


def parse_header(text: str) -> dict[str, list[str]]:
    """Return recognized metadata values from the header only."""
    found = {dimension: [] for dimension in DIMENSIONS}
    aliases = {
        alias: dimension
        for dimension, labels in DIMENSIONS.items()
        for alias in labels
    }
    for line in text.splitlines()[:40]:
        if line.strip() == "---":
            break
        match = FIELD_RE.match(line)
        if not match:
            continue
        dimension = aliases.get(match.group("label").strip())
        if dimension:
            found[dimension].append(match.group("value").strip())
    return found


def inspect_spec(path: Path) -> tuple[dict[str, str], list[str]]:
    raw = parse_header(path.read_text(encoding="utf-8"))
    values: dict[str, str] = {}
    issues: list[str] = []
    for dimension, entries in raw.items():
        if not entries:
            values[dimension] = "NOT DECLARED"
            issues.append(f"{dimension}=NOT_DECLARED")
        elif len(entries) > 1:
            values[dimension] = "AMBIGUOUS"
            issues.append(f"{dimension}=AMBIGUOUS({len(entries)} aliases)")
        else:
            values[dimension] = entries[0] or "EMPTY"
            if not entries[0]:
                issues.append(f"{dimension}=EMPTY")
    return values, issues


def numbered_specs() -> list[Path]:
    paths = []
    for path in SPEC_DIR.glob("[0-9][0-9]_*.md"):
        number = int(path.name[:2])
        if 1 <= number <= 34:
            paths.append(path)
    return sorted(paths, key=lambda path: int(path.name[:2]))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="return non-zero for undeclared, empty, or ambiguous dimensions")
    args = parser.parse_args(argv)

    specs = numbered_specs()
    print(f"Lifecycle header audit: {len(specs)} numbered specifications (01–34)")
    total_issues = 0
    for path in specs:
        values, issues = inspect_spec(path)
        state = "PASS" if not issues else "REVIEW"
        total_issues += len(issues)
        print(f"[{state}] {path.name}")
        for dimension, value in values.items():
            print(f"  {dimension}: {value}")
        for issue in issues:
            print(f"  ISSUE: {issue}")

    print(f"SUMMARY: specifications={len(specs)} metadata_issues={total_issues}")
    if args.strict and total_issues:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
