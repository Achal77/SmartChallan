import os
import tempfile
import unittest
from datetime import datetime

import numpy as np

from challan_generator import _text_challan
from detector import COLOURS, ViolationDetector, _fake_plate


class DetectorTests(unittest.TestCase):
    def test_all_supported_violations_have_colours(self):
        self.assertEqual(set(COLOURS), {
            "No Helmet", "Triple Riding", "Red Light Jump", "Number Plate"
        })

    def test_overlap_detects_significant_intersection(self):
        self.assertTrue(ViolationDetector._overlap((0, 0, 100, 100), (10, 10, 50, 50)))
        self.assertFalse(ViolationDetector._overlap((0, 0, 10, 10), (20, 20, 30, 30)))

    def test_fake_plate_matches_expected_format(self):
        self.assertRegex(_fake_plate(), r"^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$")

    def test_helmet_helper_handles_image(self):
        dark_head = np.zeros((20, 20, 3), dtype=np.uint8)
        bright_head = np.full((20, 20, 3), 255, dtype=np.uint8)
        self.assertTrue(ViolationDetector._has_helmet(dark_head))
        self.assertFalse(ViolationDetector._has_helmet(bright_head))


class ChallanTests(unittest.TestCase):
    def test_text_challan_contains_required_fields(self):
        text = _text_challan(
            "CH001", "No Helmet", "24BAI10839", 0.91,
            datetime(2026, 9, 18, 12, 30),
        )
        for value in ("CH001", "No Helmet", "24BAI10839", "91.0%", "INR 1,000/-"):
            self.assertIn(value, text)


if __name__ == "__main__":
    unittest.main()