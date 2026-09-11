import unittest
from tariff_analysis import (calculate_flat_rate_bill, calculate_tiered_bill, calculate_saving_suggestion)

class TestTariffAnalysis(unittest.TestCase):

    #Flat-rate tests
    def test_flat_rate_bill(self):
        result = calculate_flat_rate_bill(350, 0.30, 10)
        self.assertEqual(result, 115)

    def test_flat_rate_zero_consumption(self):
        result = calculate_flat_rate_bill(0, 0.30, 10)
        self.assertEqual(result, 10)

    def test_flat_rate_negative_consumption(self):
        with self.assertRaises(ValueError):
            calculate_flat_rate_bill(-50, 0.30, 10)


    #Tiered tariff tests
    tiers = [
        (100, 0.20),
        (300, 0.30),
        (500, 0.40)
    ]

    def test_tiered_bill(self):
        result = calculate_tiered_bill(350, self.tiers, 10)
        self.assertEqual(result, 110)

    def test_tiered_zero_consumption(self):
        result = calculate_tiered_bill(0, self.tiers, 10)
        self.assertEqual(result, 10)

    def test_tiered_negative_consumption(self):
        with self.assertRaises(ValueError):
            calculate_tiered_bill(-100, self.tiers, 10)


    #Savings tests
    def test_saving_exists(self):
        result = calculate_saving_suggestion(150, 110)
        self.assertEqual(result, 40)

    def test_no_saving(self):
        result = calculate_saving_suggestion(100, 120)
        self.assertEqual(result, 0)

    def test_equal_cost(self):
        result = calculate_saving_suggestion(100, 100)
        self.assertEqual(result, 0)

    def test_negative_current_cost(self):
        with self.assertRaises(ValueError):
            calculate_saving_suggestion(-100, 80)

    def test_negative_alternative_cost(self):
        with self.assertRaises(ValueError):
            calculate_saving_suggestion(100, -80)


if __name__ == "__main__":
    unittest.main()
    
# python -m unittest test_tariffanalysis.py