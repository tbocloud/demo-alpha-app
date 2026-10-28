# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

"""Submitted invoice items whose margin is under the threshold in Alpha Discount Settings."""

import frappe
from frappe import _
from frappe.utils import flt


def execute(filters=None):
	filters = filters or {}
	threshold = flt(frappe.db.get_single_value("Alpha Discount Settings", "low_margin_threshold")) or 10
	conditions = {"docstatus": 1, "margin_percent": [">", threshold]}
	if filters.get("customer"):
		invoices = frappe.get_all("Sales Invoice", filters={"customer": filters["customer"]}, pluck="name")
		conditions["parent"] = ["in", invoices or [""]]
	data = frappe.get_all(
		"Sales Invoice Item",
		filters=conditions,
		fields=["parent as invoice", "item_code", "qty", "rate", "buying_rate", "margin_percent"],
		order_by="margin_percent asc",
	)
	columns = [
		{
			"fieldname": "invoice",
			"label": _("Invoice"),
			"fieldtype": "Link",
			"options": "Sales Invoice",
			"width": 180,
		},
		{"fieldname": "item_code", "label": _("Item"), "fieldtype": "Link", "options": "Item", "width": 160},
		{"fieldname": "qty", "label": _("Qty"), "fieldtype": "Float", "width": 80},
		{"fieldname": "rate", "label": _("Rate"), "fieldtype": "Currency", "width": 110},
		{"fieldname": "buying_rate", "label": _("Buying Rate"), "fieldtype": "Currency", "width": 110},
		{"fieldname": "margin_percent", "label": _("Margin %"), "fieldtype": "Percent", "width": 100},
	]
	return columns, data
