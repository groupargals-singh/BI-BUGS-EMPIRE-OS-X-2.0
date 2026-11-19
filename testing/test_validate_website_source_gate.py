"""Unit tests for the owner-controlled website source decision gate."""
import unittest

from scripts.validate_website_source_gate import evaluate, is_https_url


def workbook(url, ownership, delivery, evidence="Owner: Project Owner; date: 2026-11-17; evidence: written approval"):
    return f"""# Workbook
| Field | Current value | Required evidence/action |
|---|---|---|
| Official website URL | {url} | |
| Website ownership | {ownership} | |
| Delivery path | {delivery} | |
| Owner decision evidence | {evidence} | |
"""


class WebsiteSourceGateTests(unittest.TestCase):
    def test_existing_site_requires_https_owner_verification_and_approved_route(self):
        passed, reasons, route = evaluate(workbook(
            "https://example.com", "OWNER VERIFIED",
            "OWNER APPROVED — EXISTING_SITE_AUDIT"
        ))
        self.assertTrue(passed, reasons)
        self.assertEqual(route, "EXISTING WEBSITE")

    def test_new_build_requires_explicit_no_site_confirmation(self):
        passed, reasons, route = evaluate(workbook(
            "NO OFFICIAL WEBSITE — OWNER CONFIRMED",
            "NOT APPLICABLE — NO OFFICIAL WEBSITE",
            "OWNER APPROVED — NEW_WEBSITE_BUILD"
        ))
        self.assertTrue(passed, reasons)
        self.assertEqual(route, "NEW WEBSITE BUILD")

    def test_unknown_values_keep_gate_blocked(self):
        passed, reasons, route = evaluate(workbook(
            "UNKNOWN", "NOT VERIFIED", "BLOCKED", "UNKNOWN"
        ))
        self.assertFalse(passed)
        self.assertEqual(route, "BLOCKED")
        self.assertGreaterEqual(len(reasons), 4)

    def test_existing_site_without_ownership_proof_is_blocked(self):
        passed, reasons, _ = evaluate(workbook(
            "https://example.com", "NOT VERIFIED",
            "OWNER APPROVED — EXISTING_SITE_AUDIT"
        ))
        self.assertFalse(passed)
        self.assertTrue(any("ownership" in reason.lower() for reason in reasons))

    def test_route_and_source_must_agree(self):
        passed, reasons, _ = evaluate(workbook(
            "NO OFFICIAL WEBSITE — OWNER CONFIRMED",
            "NOT APPLICABLE — NO OFFICIAL WEBSITE",
            "OWNER APPROVED — EXISTING_SITE_AUDIT"
        ))
        self.assertFalse(passed)
        self.assertTrue(any("Delivery path" in reason for reason in reasons))

    def test_owner_evidence_is_required(self):
        passed, reasons, _ = evaluate(workbook(
            "NO OFFICIAL WEBSITE — OWNER CONFIRMED",
            "NOT APPLICABLE — NO OFFICIAL WEBSITE",
            "OWNER APPROVED — NEW_WEBSITE_BUILD", "Owner: X"
        ))
        self.assertFalse(passed)
        self.assertTrue(any("evidence" in reason.lower() for reason in reasons))

    def test_http_and_malformed_urls_are_rejected(self):
        self.assertFalse(is_https_url("http://example.com"))
        self.assertFalse(is_https_url("https://"))
        self.assertFalse(is_https_url("https://bad host.example"))

    def test_missing_workbook_fields_are_detected(self):
        passed, reasons, _ = evaluate("# no decision table")
        self.assertFalse(passed)
        self.assertEqual(len(reasons), 4)


if __name__ == "__main__":
    unittest.main()
