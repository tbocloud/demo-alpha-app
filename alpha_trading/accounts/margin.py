# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

"""Margins on sales invoice items."""

import frappe
from frappe.utils import flt


def margin_percent(rate, buying_rate):
	"""The share of the selling price that is margin, in percent; None without a buying rate."""
	if not flt(buying_rate):
		return None
	return flt((flt(rate) - flt(buying_rate)) / flt(buying_rate) * 100, 2)


def set_margins(doc, method=None):
	"""Sales Invoice validate: each item's buying rate (the item's valuation rate unless entered) and margin."""
	for item in doc.items:
		if not flt(item.get("buying_rate")) and item.item_code:
			item.buying_rate = flt(frappe.db.get_value("Item", item.item_code, "valuation_rate"))
		item.margin_percent = margin_percent(item.rate, item.get("buying_rate"))
