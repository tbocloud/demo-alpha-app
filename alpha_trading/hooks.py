# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

app_name = "alpha_trading"
app_title = "Alpha Trading"
app_publisher = "Team Back Office"
app_description = "Margins and volume discounts for Alpha Trading"
app_email = "support@teambackoffice.com"
app_license = "mit"
required_apps = ["erpnext"]

after_install = "alpha_trading.install.after_install"
after_migrate = "alpha_trading.install.after_install"

doc_events = {
	"Sales Invoice": {
		"validate": "alpha_trading.accounts.margin.set_margins",
	},
	"Quotation": {
		"before_insert": "alpha_trading.selling.discounts.set_default_price_list",
		"validate": "alpha_trading.selling.discounts.apply_tier_discounts",
	},
}
