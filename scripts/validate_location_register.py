#!/usr/bin/env python3
"""Validate BI-BUGS owner-selected locations without asserting service coverage."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "docs" / "MASTER_SPECIFICATION" / "LOCATION_AREA_REGISTER.json"
EXPECTED_DIVISIONS = {
    "Chambal": {"Morena", "Bhind", "Sheopur"},
    "Gwalior": {"Gwalior", "Shivpuri", "Guna", "Ashoknagar", "Datia"},
    "Bhopal": {"Bhopal", "Sehore", "Raisen", "Rajgarh", "Vidisha"},
    "Indore": {"Indore", "Dhar", "Jhabua", "Alirajpur", "Barwani", "Khargone", "Khandwa", "Burhanpur"},
}
EXPECTED_EXTRA = {
    ("Rajasthan", "Jaipur"), ("Rajasthan", "Jaisalmer"),
    ("Rajasthan", "Dholpur"), ("Uttar Pradesh", "Agra"),
}

def evaluate(data: dict) -> tuple[bool, list[str], int]:
    errors: list[str] = []
    if data.get("register_id") != "BBE-LOC-001":
        errors.append("Unexpected or missing register_id")
    scope = data.get("selector_scope", {})
    if scope.get("india") != "ALL_STATES_AND_UNION_TERRITORIES_AND_CITIES":
        errors.append("India selector scope must include all States/UTs and cities")
    if scope.get("international") != "SEPARATE_COUNTRY_SELECTOR":
        errors.append("International selector must remain a separate country selector")
    if scope.get("unselected_locations_default") != "INACTIVE" or scope.get("unselected_locations_remain_selectable") is not True:
        errors.append("Unselected locations must remain selectable but default to inactive")
    policy = data.get("coverage_policy", {})
    if policy.get("service_availability_default") != "UNVERIFIED":
        errors.append("Service availability default must remain UNVERIFIED")
    if policy.get("active_area_is_not_service_availability") is not True:
        errors.append("Active-area/service-availability separation must be explicit")
    divisions = data.get("active_divisions", [])
    names = {item.get("division") for item in divisions}
    if names != set(EXPECTED_DIVISIONS):
        errors.append(f"Expected exactly the four selected MP divisions; found {sorted(str(x) for x in names)}")
    seen_ids: set[str] = set()
    selected_districts: set[tuple[str, str]] = set()
    for item in divisions:
        rid = item.get("id", "<missing-id>")
        if rid in seen_ids:
            errors.append(f"Duplicate location id: {rid}")
        seen_ids.add(rid)
        if item.get("country") != "IN" or item.get("state") != "Madhya Pradesh":
            errors.append(f"{rid}: MP division has incorrect country/state")
        if item.get("selection_status") != "ACTIVE_OWNER_SELECTED":
            errors.append(f"{rid}: division is not marked owner-selected active")
        division = item.get("division")
        districts = item.get("districts", [])
        if len(districts) != len(set(districts)):
            errors.append(f"{rid}: duplicate district in division")
        if set(districts) != EXPECTED_DIVISIONS.get(division, set()):
            errors.append(f"{rid}: district list does not match the recorded owner-selected division mapping")
        selected_districts.update(("Madhya Pradesh", d) for d in districts)
    extras = data.get("additional_active_districts", [])
    for item in extras:
        rid = item.get("id", "<missing-id>")
        if rid in seen_ids:
            errors.append(f"Duplicate location id: {rid}")
        seen_ids.add(rid)
        pair = (item.get("state"), item.get("district"))
        if pair not in EXPECTED_EXTRA:
            errors.append(f"{rid}: unexpected additional active district {pair}")
        selected_districts.add(pair)
        if item.get("country") != "IN":
            errors.append(f"{rid}: selected Indian district must use country IN")
        if item.get("selection_status") not in {"ACTIVE_OWNER_SELECTED", "ACTIVE_OWNER_SELECTED_PRIOR_INPUT"}:
            errors.append(f"{rid}: invalid active selection status")
    if {x for x in selected_districts if x[0] != "Madhya Pradesh"} != EXPECTED_EXTRA:
        errors.append("Additional active districts do not match Rajasthan Jaipur/Jaisalmer/Dholpur and Uttar Pradesh Agra")
    if len(selected_districts) != 25:
        errors.append(f"Expected 25 unique active districts total; found {len(selected_districts)}")
    coverage = data.get("service_coverage", {})
    if coverage.get("status") != "UNVERIFIED":
        errors.append("District-level service coverage must remain UNVERIFIED until separately evidenced")
    if data.get("data_governance", {}).get("authoritative_admin_boundaries_required_for_full_selector") is not True:
        errors.append("Full selector must require authoritative administrative-boundary data")
    return not errors, errors, len(selected_districts)

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--register", type=Path, default=REGISTER)
    parser.add_argument("--strict", action="store_true", help="fail on any register integrity issue")
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.register.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Location register: FAIL — {exc}")
        return 1 if args.strict else 0
    passed, errors, count = evaluate(data)
    print(f"Location register: {'PASS' if passed else 'FAIL'}")
    print(f"Owner-selected active districts: {count}/25")
    print("Selector scope and service-availability separation are validated; this does not verify live coverage or implement a website selector.")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if args.strict and not passed else 0

if __name__ == "__main__":
    sys.exit(main())
