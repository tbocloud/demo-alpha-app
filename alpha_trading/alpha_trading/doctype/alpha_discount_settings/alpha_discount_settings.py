# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class AlphaDiscountSettings(Document):
	def get_minimum_margin(self):
		return self.low_margin_threshold or 0
