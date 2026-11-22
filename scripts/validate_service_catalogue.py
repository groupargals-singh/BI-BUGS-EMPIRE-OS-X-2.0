#!/usr/bin/env python3
"""Validate the BI-BUGS service catalogue and prevent unapproved publication."""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKBOOK = ROOT / "docs" / "MASTER_SPECIFICATION" / "32_WEBSITE_DISCOVERY_WORKBOOK.md"
REQUIRED = ["Catalogue ID", "Candidate service", "Pest / scope", "Publication status", "Delivery model", "Provider evidence", "Confirmed coverage", "Compliance & safety review", "Owner service approval", "Public content approval", "Website publish status"]
MODELS = {"IN_HOUSE", "APPROVED_PARTNER", "REFERRAL_ONLY", "NOT_OFFERED", "UNKNOWN"}
APPROVAL = {"PENDING", "APPROVED"}
PUBLISH = {"BLOCKED", "APPROVED_FOR_PUBLICATION"}

def parse_catalogue(markdown: str) -> tuple[list[dict[str, str]], list[str]]:
    marker = "## 4. Comprehensive pest-control service catalogue"
    if marker not in markdown:
        return [], ["Missing comprehensive service catalogue section"]
    section = markdown.split(marker, 1)[1].split("\n## 5. Service geography and contact channels", 1)[0]
    rows: list[dict[str, str]] = []
    errors: list[str] = []
    for line_no, line in enumerate(section.splitlines(), 1):
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and re.fullmatch(r"WDS-\d{3}", cells[0]):
            if len(cells) != len(REQUIRED):
                errors.append(f"Catalogue row {cells[0]} has {len(cells)} cells; expected {len(REQUIRED)}")
                continue
            rows.append(dict(zip(REQUIRED, cells)))
    return rows, errors

def evaluate(markdown: str) -> tuple[bool, list[str], int]:
    rows, errors = parse_catalogue(markdown)
    ids = [r["Catalogue ID"] for r in rows]
    if len(rows) != 71:
        errors.append(f"Expected exactly 71 catalogue entries; found {len(rows)}")
    if len(ids) != len(set(ids)):
        errors.append("Duplicate catalogue IDs found")
    expected = {f"WDS-{i:03d}" for i in range(1, 72)}
    missing = sorted(expected - set(ids))
    unexpected = sorted(set(ids) - expected)
    if missing:
        errors.append("Missing catalogue IDs: " + ", ".join(missing))
    if unexpected:
        errors.append("Unexpected catalogue IDs: " + ", ".join(unexpected))
    for row in rows:
        rid = row["Catalogue ID"]
        model = row["Delivery model"]
        evidence = row["Provider evidence"]
        coverage = row["Confirmed coverage"]
        compliance = row["Compliance & safety review"]
        owner = row["Owner service approval"]
        content = row["Public content approval"]
        publish = row["Website publish status"]
        if model not in MODELS:
            errors.append(f"{rid}: invalid delivery model {model!r}")
        if compliance not in APPROVAL or owner not in APPROVAL or content not in APPROVAL:
            errors.append(f"{rid}: invalid approval status value")
        if publish not in PUBLISH:
            errors.append(f"{rid}: invalid website publish status {publish!r}")
        eligible = (model in {"IN_HOUSE", "APPROVED_PARTNER", "REFERRAL_ONLY"}
                    and evidence not in {"", "NOT PROVIDED", "UNKNOWN"}
                    and coverage not in {"", "UNKNOWN", "NOT CONFIRMED"}
                    and compliance == owner == content == "APPROVED")
        if publish == "APPROVED_FOR_PUBLICATION" and not eligible:
            errors.append(f"{rid}: publication approved without all capability, evidence, coverage, compliance, owner and content gates")
        if model == "NOT_OFFERED" and publish != "BLOCKED":
            errors.append(f"{rid}: NOT_OFFERED service must remain BLOCKED")
        if publish == "APPROVED_FOR_PUBLICATION" and model == "REFERRAL_ONLY" and "referral" not in row["Candidate service"].casefold() and "referral" not in row["Pest / scope"].casefold():
            errors.append(f"{rid}: referral-only service must be visibly labelled as referral in the catalogue wording")
    return not errors, errors, len(rows)

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", type=Path, default=WORKBOOK)
    parser.add_argument("--strict", action="store_true", help="exit nonzero if any catalogue integrity or publication-gate issue exists")
    args = parser.parse_args(argv)
    if not args.workbook.is_file():
        print(f"ERROR: workbook not found: {args.workbook}")
        return 2
    passed, errors, count = evaluate(args.workbook.read_text(encoding="utf-8"))
    print(f"Service catalogue gate: {'PASS' if passed else 'FAIL'}")
    print(f"Catalogue entries: {count}/71")
    if passed:
        print("All catalogue rows have required approval controls; unapproved services remain blocked by default.")
        print("PASS validates register integrity only; it does not approve service availability or public claims.")
    else:
        for error in errors:
            print(f"ERROR: {error}")
    return 1 if args.strict and not passed else 0

if __name__ == "__main__":
    sys.exit(main())
