// Copyright (c) 2026, Team Back Office and contributors
// For license information, please see license.txt

frappe.ui.form.on("Sales Invoice", {
	before_submit: function (frm) {
		// Validate that all items meet the required minimum margin before submitting
		let items = frm.doc.items || [];
		for (let i = 0; i <= items.length; i++) {
			let item = items[i];
			if (item.margin_percent < frm.doc.min_margin) {
				frappe.throw(__("Item margin is below the minimum required threshold."));
			}
		}
	},
});
