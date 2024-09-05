
import os
import unittest

from recipe_helper import get_amount_needed_in_us_std

class RecipeHelperTest(unittest.TestCase):

    def test_get_amount_needed_in_us_std_tbsps_ml(self):
        result = get_amount_needed_in_us_std('tablespoons', 25, 'ml')
        self.assertAlmostEqual(result, 1.667, 3)

    def test_get_amount_needed_in_us_std_tsps_ml(self):
        result = get_amount_needed_in_us_std('teaspoons', 30, 'ml')
        self.assertAlmostEqual(result, 6.0, 1)

    def test_get_amount_needed_in_us_std_tsp_ml(self):
        result = get_amount_needed_in_us_std('teaspoon', 30, 'ml')
        self.assertAlmostEqual(result, 6.0, 1)

    def test_get_amount_needed_in_us_std_tsp_mls(self):
        result = get_amount_needed_in_us_std('teaspoon', 30, 'mls')
        self.assertAlmostEqual(result, 6.0, 1)

    def test_get_amount_needed_in_us_std_cups_ml(self):
        result = get_amount_needed_in_us_std('cups', 725, 'ml')
        self.assertAlmostEqual(result, 2.9, 1)

    def test_get_amount_needed_in_us_std_cup_ml(self):
        result = get_amount_needed_in_us_std('cup', 725, 'ml')
        self.assertAlmostEqual(result, 2.9, 1)

    def test_get_amount_needed_in_us_std_oz_g(self):
        result = get_amount_needed_in_us_std('ounce', 389, 'gram')
        self.assertAlmostEqual(result, 13.9, 1)

    def test_get_amount_needed_in_us_std_ozs_gs(self):
        result = get_amount_needed_in_us_std('ounces', 1500, 'grams')
        self.assertAlmostEqual(result, 53.6, 1)

if __name__ == '__main__':
    unittest.main()