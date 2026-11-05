import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_rates_at_other_weights(self):
        for weight, local, regional in [(1, 6.5, 9.5), (0.75, 6.12, 9.12)]:
            for zone, expected in [("local", local), ("regional", regional)]:
                with self.subTest(weight=weight, zone=zone):
                    self.assertEqual(shipping_quote(weight, zone), expected)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")
