"""Tests for owner-selected location register integrity and coverage safeguards."""
import copy
import json
import unittest
from pathlib import Path
from scripts.validate_location_register import evaluate, REGISTER

class LocationRegisterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(REGISTER.read_text(encoding="utf-8"))

    def test_repository_register_has_25_selected_districts(self):
        passed, errors, count = evaluate(self.data)
        self.assertTrue(passed, errors)
        self.assertEqual(count, 25)

    def test_missing_district_fails(self):
        data = copy.deepcopy(self.data)
        data["active_divisions"][0]["districts"].remove("Bhind")
        passed, errors, _ = evaluate(data)
        self.assertFalse(passed)
        self.assertTrue(any("district list" in e for e in errors))

    def test_duplicate_location_id_fails(self):
        data = copy.deepcopy(self.data)
        data["additional_active_districts"][0]["id"] = data["active_divisions"][0]["id"]
        passed, errors, _ = evaluate(data)
        self.assertFalse(passed)
        self.assertTrue(any("Duplicate location id" in e for e in errors))

    def test_active_area_cannot_be_treated_as_service_availability(self):
        data = copy.deepcopy(self.data)
        data["service_coverage"]["status"] = "AVAILABLE"
        passed, errors, _ = evaluate(data)
        self.assertFalse(passed)
        self.assertTrue(any("UNVERIFIED" in e for e in errors))

    def test_unselected_locations_default_inactive(self):
        data = copy.deepcopy(self.data)
        data["selector_scope"]["unselected_locations_default"] = "ACTIVE"
        passed, errors, _ = evaluate(data)
        self.assertFalse(passed)
        self.assertTrue(any("default to inactive" in e for e in errors))

    def test_international_selector_is_separate(self):
        data = copy.deepcopy(self.data)
        data["selector_scope"]["international"] = "MIXED_WITH_INDIA"
        passed, errors, _ = evaluate(data)
        self.assertFalse(passed)
        self.assertTrue(any("separate country selector" in e for e in errors))

if __name__ == "__main__":
    unittest.main()
