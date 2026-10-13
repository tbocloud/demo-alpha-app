# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

"""The fields Alpha Trading adds to ERPNext's documents."""

from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

FIELDS = {
	"Sales Invoice Item": [
		{
			"fieldname": "buying_rate",
			"label": "Buying Rate",
			"fieldtype": "Currency",
			"insert_after": "rate",
			"description": "What the item cost; the item's valuation rate unless entered.",
		},
		{
			"fieldname": "margin_percent",
			"label": "Margin %",
			"fieldtype": "Percent",
			"insert_after": "buying_rate",
			"read_only": 1,
			"description": "The share of the selling price that is margin.",
		},
	],
	"Quotation Item": [
		{
			"fieldname": "tier_discount_percent",
			"label": "Volume Discount %",
			"fieldtype": "Percent",
			"insert_after": "discount_percentage",
			"description": "From the volume discount tiers in Alpha Discount Settings, set when the quotation is saved.",
		},
	],
}


def after_install():
	create_custom_fields(FIELDS, update=True)
