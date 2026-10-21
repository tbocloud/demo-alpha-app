# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

"""Margins on sales invoice items."""

import frappe
from frappe.utils import flt


def margin_percent(rate, buying_rate):
	"""The share of the selling price that is margin, in percent; None without a buying or a selling rate.

	Bought at 100 and sold at 125: 25 of the 125 is margin, 20%. (25 of the 100 cost, 25%, is the markup.)
	"""
	if not flt(buying_rate) or not flt(rate):
		return None
	return flt((flt(rate) - flt(buying_rate)) / flt(rate) * 100, 2)


def set_margins(doc, method=None):
	"""Sales Invoice validate: each item's buying rate (the item's valuation rate unless entered) and margin."""
	for item in doc.items:
		if not flt(item.get("buying_rate")) and item.item_code:
			item.buying_rate = flt(frappe.db.get_value("Item", item.item_code, "valuation_rate"))
		item.margin_percent = margin_percent(item.rate, item.get("buying_rate"))


def validate_margin_on_submit(doc, method=None):
	"""Sales Invoice before_submit: check that invoice items meet the minimum margin threshold."""
	for item in doc.items:
		if item.margin_percent < doc.min_margin:
			frappe.throw(frappe._("Margin is below the required minimum."))

