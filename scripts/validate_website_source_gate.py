#!/usr/bin/env python3
"""Validate the owner-controlled BI-BUGS website source decision gate.

This is a read-only gate check. It never changes the discovery workbook and
does not certify that the full website requirements or release are approved.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
WORKBOOK = ROOT / "docs" / "MASTER_SPECIFICATION" / "32_WEBSITE_DISCOVERY_WORKBOOK.md"

UNKNOWN_VALUES = {"", "UNKNOWN", "NOT VERIFIED", "BLOCKED", "TBD"}
NO_SITE = "NO OFFICIAL WEBSITE — OWNER CONFIRMED"
NOT_APPLICABLE = "NOT APPLICABLE — NO OFFICIAL WEBSITE"
EXISTING_PATHS = {
    "OWNER APPROVED — EXISTING_SITE_AUDIT",
    "OWNER APPROVED — MIGRATION",
    "OWNER APPROVED — REDESIGN",
}
NEW_BUILD_PATH = "OWNER APPROVED — NEW_WEBSITE_BUILD"


def table_value(markdown: str, field: str) -> str | None:
    """Return the second cell from the first Markdown table row for field."""
    for line in markdown.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0].casefold() == field.casefold():
            return cells[1]
    return None


def is_https_url(value: str) -> bool:
    try:
        parsed = urlsplit(value)
        return (
            parsed.scheme == "https"
            and bool(parsed.hostname)
            and not any(ch.isspace() for ch in value)
        )
    except ValueError:
        return False


def evaluate(markdown: str) -> tuple[bool, list[str], str]:
    """Return (passed, reasons, selected delivery route)."""
    reasons: list[str] = []
    url = table_value(markdown, "Official website URL")
    ownership = table_value(markdown, "Website ownership")
    delivery = table_value(markdown, "Delivery path")
    evidence = table_value(markdown, "Owner decision evidence")

    for label, value in (
        ("Official website URL", url),
        ("Website ownership", ownership),
        ("Delivery path", delivery),
        ("Owner decision evidence", evidence),
    ):
        if value is None:
            reasons.append(f"Missing workbook field: {label}")
        elif value.strip().upper() in UNKNOWN_VALUES:
            reasons.append(f"{label} is unresolved")

    if reasons:
        return False, reasons, "BLOCKED"

    assert url is not None and ownership is not None
    assert delivery is not None and evidence is not None
    if len(evidence.strip()) < 12:
        reasons.append("Owner decision evidence must identify approver, date, and evidence/reference")

    if url == NO_SITE:
        if ownership != NOT_APPLICABLE:
            reasons.append("No-site decision requires Website ownership = NOT APPLICABLE — NO OFFICIAL WEBSITE")
        if delivery != NEW_BUILD_PATH:
            reasons.append("No-site decision requires Delivery path = OWNER APPROVED — NEW_WEBSITE_BUILD")
        route = "NEW WEBSITE BUILD"
    elif is_https_url(url):
        if ownership != "OWNER VERIFIED":
            reasons.append("Existing URL requires Website ownership = OWNER VERIFIED")
        if delivery not in EXISTING_PATHS:
            reasons.append("Existing URL requires an owner-approved existing-site audit, migration, or redesign path")
        route = "EXISTING WEBSITE"
    else:
        reasons.append("Official website URL must be a valid HTTPS URL or the exact owner-confirmed no-site value")
        route = "BLOCKED"

    return not reasons, reasons, route


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", type=Path, default=WORKBOOK)
    parser.add_argument("--strict", action="store_true", help="exit 1 while the owner source decision remains blocked")
    args = parser.parse_args(argv)

    if not args.workbook.is_file():
        print(f"ERROR: workbook not found: {args.workbook}")
        return 2

    passed, reasons, route = evaluate(args.workbook.read_text(encoding="utf-8"))
    print(f"Website source gate: {'PASS' if passed else 'BLOCKED'}")
    print(f"Selected route: {route}")
    if passed:
        print("Owner source decision fields are complete. This does NOT approve the full requirements, implementation, or production release.")
    else:
        for reason in reasons:
            print(f"BLOCKER: {reason}")
    return 1 if args.strict and not passed else 0


if __name__ == "__main__":
    sys.exit(main())
