# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

from frappe.tests.utils import FrappeTestCase

from alpha_trading.selling.discounts import tier_for

TIERS = [
	{"min_qty": 50, "discount_percent": 10},
	{"min_qty": 10, "discount_percent": 5},
]


class TestVolumeDiscount(FrappeTestCase):
	def test_below_the_first_tier_there_is_no_discount(self):
		self.assertEqual(tier_for(5, TIERS), 0)

	def test_between_two_tiers_the_lower_one_applies(self):
		self.assertEqual(tier_for(20, TIERS), 5)
	def test_at_a_tier_minimum_the_tier_applies(self):
		self.assertEqual(tier_for(50, TIERS), 10)

	def test_above_the_top_tier_the_top_discount_applies(self):
		self.assertEqual(tier_for(120, TIERS), 10)

	def test_no_tiers_no_discount(self):
		self.assertEqual(tier_for(100, []), 0)
