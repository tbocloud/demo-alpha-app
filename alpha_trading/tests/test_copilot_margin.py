# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

from alpha_trading.accounts.margin import validate_margin_on_submit


class TestCopilotMargin(FrappeTestCase):
	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		frappe.db.set_single_value("Alpha Discount Settings", "low_margin_threshold", 10)

	def test_sales_invoice_margin_above_configured_threshold_submits(self):
		invoice = type("Invoice", (), {"items": [frappe._dict({"margin_percent": 20})]})()

		try:
			validate_margin_on_submit(invoice)
		except AttributeError as error:
			self.fail(f"Sales Invoice margin validation raised an unexpected error: {error}")

	def test_sales_invoice_margin_below_configured_threshold_is_rejected(self):
		invoice = type("Invoice", (), {"items": [frappe._dict({"margin_percent": 5})]})()

		try:
			with self.assertRaises(frappe.ValidationError):
				validate_margin_on_submit(invoice)
		except AttributeError as error:
			self.fail(f"Sales Invoice margin validation raised an unexpected error: {error}")
