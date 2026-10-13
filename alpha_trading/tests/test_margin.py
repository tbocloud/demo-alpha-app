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
