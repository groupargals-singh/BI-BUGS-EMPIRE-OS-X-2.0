"""Tests for the imported location reference catalogue."""
import unittest
from scripts.validate_location_catalogue import validate

class LocationCatalogueTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.errors, cls.metrics = validate()

    def test_imported_catalogues_pass_integrity_validation(self):
        self.assertEqual(self.errors, [])

    def test_india_administrative_hierarchy_is_complete_for_snapshot(self):
        self.assertEqual(self.metrics.get('state_ut_count'), 36)
        self.assertEqual(self.metrics.get('state_count'), 28)
        self.assertEqual(self.metrics.get('ut_count'), 8)
        self.assertEqual(self.metrics.get('district_count'), 770)

    def test_un_m49_separate_international_list(self):
        self.assertEqual(self.metrics.get('un_m49_country_area_count'), 248)
        self.assertEqual(self.metrics.get('international_country_area_count'), 247)

    def test_populated_place_index_has_large_india_search_coverage(self):
        self.assertGreater(self.metrics.get('populated_place_count', 0), 500000)
        self.assertGreater(self.metrics.get('state_mapped_place_count', 0), 500000)

if __name__=='__main__':unittest.main()
