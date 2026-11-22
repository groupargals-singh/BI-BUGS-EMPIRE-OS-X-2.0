"""Unit tests for the read-only lifecycle metadata audit."""
import unittest

from scripts.validate_spec_lifecycle import parse_header, inspect_spec, numbered_specs


class LifecycleHeaderTests(unittest.TestCase):
    def test_numbered_specification_35_is_in_audit_scope(self):
        names = {path.name for path in numbered_specs()}
        self.assertIn("35_LOCATION_CATALOGUE_AND_COVERAGE_GOVERNANCE.md", names)

    def test_canonical_fields_are_read(self):
        header = """# Example
**Specification status:** DRAFT FOR REVIEW
**Implementation status:** NOT STARTED
**Testing status:** NOT RUN
**Production status:** NOT VERIFIED
---
"""
        values = parse_header(header)
        self.assertEqual(values["Specification status"], ["DRAFT FOR REVIEW"])
        self.assertEqual(values["Implementation status"], ["NOT STARTED"])
        self.assertEqual(values["Testing status"], ["NOT RUN"])
        self.assertEqual(values["Production status"], ["NOT VERIFIED"])

    def test_legacy_aliases_are_read_without_upgrading_values(self):
        header = """# Legacy
**Status:** ACTIVE
**Implementation:** NOT STARTED
**Testing:** NOT RUN
**Production:** NOT STARTED
---
"""
        values = parse_header(header)
        self.assertEqual(values["Specification status"], ["ACTIVE"])
        self.assertEqual(values["Implementation status"], ["NOT STARTED"])

    def test_missing_fields_are_not_inferred(self):
        header = """# Old document
**Status:** ACTIVE
---
"""
        values = parse_header(header)
        self.assertEqual(values["Specification status"], ["ACTIVE"])
        self.assertEqual(values["Testing status"], [])

    def test_duplicate_aliases_are_flagged_ambiguous(self):
        from pathlib import Path
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.md"
            path.write_text("# Example\n**Status:** ACTIVE\n**Specification status:** DRAFT\n---\n")
            values, issues = inspect_spec(path)
        self.assertEqual(values["Specification status"], "AMBIGUOUS")
        self.assertTrue(any("AMBIGUOUS" in issue for issue in issues))

    def test_body_mentions_do_not_count_as_header_fields(self):
        header = """# Example
---
This body mentions **Testing status:** PASS.
"""
        values = parse_header(header)
        self.assertEqual(values["Testing status"], [])


if __name__ == "__main__":
    unittest.main()
