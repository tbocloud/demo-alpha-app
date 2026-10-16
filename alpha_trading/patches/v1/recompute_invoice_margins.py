# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

"""Recompute the stored margin of every Sales Invoice Item with the corrected formula.

Margins were stored as a markup (divided by the buying rate), so the Low Margin Invoices
report, which reads the stored value, missed invoices whose real margin is under its
threshold. Margin % is a read-only, derived field: no amount, ledger entry or tax changes.
"""

import frappe

from alpha_trading.accounts.margin import margin_percent


def execute():
	for item in frappe.get_all(
		"Sales Invoice Item",
		filters={"buying_rate": [">", 0]},
		fields=["name", "rate", "buying_rate", "margin_percent"],
	):
		margin = margin_percent(item.rate, item.buying_rate)
		if margin != item.margin_percent:
			frappe.db.set_value("Sales Invoice Item", item.name, "margin_percent", margin, update_modified=False)
