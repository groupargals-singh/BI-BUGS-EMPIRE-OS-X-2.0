from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "frontend" / "index.html"
CSS = ROOT / "frontend" / "assets" / "css" / "styles.css"
JS = ROOT / "frontend" / "assets" / "js" / "main.js"


class WebsiteShellTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = HTML.read_text(encoding="utf-8")
        cls.css = CSS.read_text(encoding="utf-8")
        cls.js = JS.read_text(encoding="utf-8")

    def test_semantic_document_and_mobile_viewport(self):
        self.assertIn('<html lang="en">', self.html)
        self.assertIn('name="viewport"', self.html)
        self.assertIn('<main id="main">', self.html)
        self.assertIn("<header", self.html)
        self.assertIn("<footer", self.html)

    def test_confirmed_company_identity_is_present(self):
        self.assertIn("BI-BUGS Pest Control Services Pvt Ltd", self.html)

    def test_unapproved_business_facts_are_not_fabricated(self):
        for forbidden in ("+91", "www.", "@gmail.com", "₹", "100% guaranteed", "ISO certified"):
            self.assertNotIn(forbidden, self.html)

    def test_no_unapproved_data_collection_or_transaction_controls(self):
        self.assertNotIn("<form", self.html.lower())
        self.assertNotIn('type="password"', self.html.lower())
        self.assertNotIn("payment", self.html.lower())
        self.assertNotIn("book now", self.html.lower())

    def test_responsive_and_reduced_motion_styles_exist(self):
        self.assertIn("@media (max-width: 700px)", self.css)
        self.assertIn("@media (prefers-reduced-motion: reduce)", self.css)
        self.assertIn(":focus-visible", self.css)

    def test_mobile_navigation_updates_accessible_state(self):
        self.assertIn("aria-expanded", self.html)
        self.assertIn('aria-controls="primary-navigation"', self.html)
        self.assertIn('setAttribute("aria-expanded"', self.js)
        self.assertIn('classList.toggle("is-open"', self.js)


if __name__ == "__main__":
    unittest.main()
