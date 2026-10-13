// Copyright (c) 2026, Team Back Office and contributors
// For license information, please see license.txt

frappe.query_reports["Low Margin Invoices"] = {
	filters: [
		{
			fieldname: "customer",
			label: __("Customer"),
			fieldtype: "Link",
			options: "Customer",
		},
	],
};
