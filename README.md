# Alpha Trading

The custom app of **Alpha Trading**, a wholesale distributor of office supplies, on ERPNext 15.

Alpha Trading is a fictional company used to test TBO Support. This repository holds no real customer code or data.

## What it adds

- **Margin on sales invoices.** Each invoice item has a buying rate (the item's valuation rate unless entered) and a margin: the share of the selling price that is margin.
- **Low Margin Invoices.** A report of submitted invoice items whose margin is under the threshold in Alpha Discount Settings (10% by default).
- **Volume discounts on quotations.** Alpha Discount Settings lists discount tiers by quantity; each quotation item gets the discount of the highest tier its quantity reaches, shown as Volume Discount %.
- **Default price list.** New quotations start with the price list chosen in Alpha Discount Settings.

## Install

```
bench get-app https://github.com/tbocloud/demo-alpha-app
bench --site <site> install-app alpha_trading
```

ERPNext 15 is required. Installing adds the custom fields (buying rate, margin, volume discount) to Sales Invoice Item and Quotation Item.

## Tests

```
bench --site <site> run-tests --app alpha_trading
```
