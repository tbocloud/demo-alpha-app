# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

from frappe.tests.utils import FrappeTestCase

from alpha_trading.accounts.margin import margin_percent


class TestMargin(FrappeTestCase):
	def test_no_buying_rate_means_no_margin(self):
		self.assertIsNone(margin_percent(100, 0))
		self.assertIsNone(margin_percent(100, None))

	def test_selling_at_cost_is_no_margin(self):
		self.assertEqual(margin_percent(80, 80), 0)

	def test_margin_is_a_share_of_the_selling_price(self):
		# bought at 100 and sold at 125: 25 of 125 is 20% (25% was the markup)
		self.assertEqual(margin_percent(125, 100), 20)
		self.assertEqual(margin_percent(110, 100), 9.09)

	def test_no_selling_price_means_no_margin(self):
		self.assertIsNone(margin_percent(0, 100))
