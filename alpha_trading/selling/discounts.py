# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

"""Volume discounts and the default price list on quotations."""

import frappe
from frappe.utils import flt

SETTINGS = "Alpha Discount Settings"


def tiers() -> list[dict]:
	return frappe.get_all(
		"Alpha Discount Tier",
		filters={"parent": SETTINGS, "parenttype": SETTINGS},
		fields=["min_qty", "discount_percent"],
		order_by="min_qty asc",
	)


def tier_for(qty, discount_tiers) -> float:
	"""The discount of the highest tier the quantity reaches; 0 below the first tier."""
	discount = 0.0
	for tier in sorted(discount_tiers, key=lambda tier: flt(tier["min_qty"])):
		if flt(qty) >= flt(tier["min_qty"]):
			discount = flt(tier["discount_percent"])
	return discount


def apply_tier_discounts(doc, method=None):
	"""Quotation validate: each item's volume discount from its quantity."""
	discount_tiers = tiers()
	for item in doc.items:
		item.tier_discount_percent = tier_for(item.qty, discount_tiers)


def set_default_price_list(doc, method=None):
	"""Quotation before_insert: start with the price list chosen in Alpha Discount Settings."""
	price_list = frappe.db.get_single_value(SETTINGS, "default_price_list")
	if price_list:
		doc.selling_price_list = price_list
