"""Tests for the BI-BUGS service catalogue publication gate."""
import unittest
from pathlib import Path
from scripts.validate_service_catalogue import evaluate, parse_catalogue

WORKBOOK = Path(__file__).resolve().parents[1] / "docs/MASTER_SPECIFICATION/32_WEBSITE_DISCOVERY_WORKBOOK.md"

def sample_row(rid="WDS-001", model="UNKNOWN", evidence="NOT PROVIDED", coverage="UNKNOWN", compliance="PENDING", owner="PENDING", content="PENDING", publish="BLOCKED"):
    return f"| {rid} | General Pest Control | General household pest control | CANDIDATE — VERIFY | {model} | {evidence} | {coverage} | {compliance} | {owner} | {content} | {publish} |"

def minimal(rows):
    ids = "\n".join(rows)
    return "## 4. Comprehensive pest-control service catalogue\n| Catalogue ID | Candidate service | Pest / scope | Publication status | Delivery model | Provider evidence | Confirmed coverage | Compliance & safety review | Owner service approval | Public content approval | Website publish status |\n|---|---|---|---|---|---|---|---|---|---|---|\n" + ids + "\n## 5. Service geography and contact channels\n"

class ServiceCatalogueTests(unittest.TestCase):
    def test_repository_catalogue_has_71_safe_blocked_entries(self):
        text = WORKBOOK.read_text(encoding="utf-8")
        passed, errors, count = evaluate(text)
        self.assertTrue(passed, errors)
        self.assertEqual(count, 71)
        rows, parse_errors = parse_catalogue(text)
        self.assertFalse(parse_errors)
        self.assertTrue(all(r["Website publish status"] == "BLOCKED" for r in rows))

    def test_missing_catalogue_entry_fails(self):
        rows = [sample_row(f"WDS-{i:03d}") for i in range(1, 71)]
        passed, errors, _ = evaluate(minimal(rows))
        self.assertFalse(passed)
        self.assertTrue(any("Expected exactly 71" in e for e in errors))

    def test_duplicate_id_fails(self):
        rows = [sample_row("WDS-001") for _ in range(71)]
        passed, errors, _ = evaluate(minimal(rows))
        self.assertFalse(passed)
        self.assertTrue(any("Duplicate" in e for e in errors))

    def test_unapproved_service_cannot_be_published(self):
        rows = [sample_row("WDS-001", publish="APPROVED_FOR_PUBLICATION")] + [sample_row(f"WDS-{i:03d}") for i in range(2, 72)]
        passed, errors, _ = evaluate(minimal(rows))
        self.assertFalse(passed)
        self.assertTrue(any("without all" in e for e in errors))

    def test_all_evidence_and_approvals_are_required_for_publication(self):
        rows = [sample_row("WDS-001", "IN_HOUSE", "CAPABILITY-EVIDENCE-001", "Morena", "APPROVED", "APPROVED", "APPROVED", "APPROVED_FOR_PUBLICATION")] + [sample_row(f"WDS-{i:03d}") for i in range(2, 72)]
        passed, errors, _ = evaluate(minimal(rows))
        self.assertTrue(passed, errors)

    def test_not_offered_must_remain_blocked(self):
        rows = [sample_row("WDS-001", "NOT_OFFERED", publish="APPROVED_FOR_PUBLICATION")] + [sample_row(f"WDS-{i:03d}") for i in range(2, 72)]
        passed, errors, _ = evaluate(minimal(rows))
        self.assertFalse(passed)
        self.assertTrue(any("NOT_OFFERED" in e for e in errors))

    def test_referral_only_requires_referral_wording(self):
        rows = [sample_row("WDS-001", "REFERRAL_ONLY", "PARTNER-REF-1", "Morena", "APPROVED", "APPROVED", "APPROVED", "APPROVED_FOR_PUBLICATION")] + [sample_row(f"WDS-{i:03d}") for i in range(2, 72)]
        passed, errors, _ = evaluate(minimal(rows))
        self.assertFalse(passed)
        self.assertTrue(any("referral" in e.lower() for e in errors))

if __name__ == "__main__":
    unittest.main()
