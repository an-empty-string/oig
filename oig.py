#!/usr/bin/env python3
import arrow
import decimal
import jinja2
import sys
import yaml

invoice = yaml.safe_load(sys.stdin)
for item in invoice["items"]:
    item["date"] = arrow.get(item["date"])
    item["hours"] = decimal.Decimal(item["hours"])
    item["rate"] = decimal.Decimal(item["rate"])
    item["total"] = item["hours"] * item["rate"]

for key in ("date", "start_date", "end_date",):
    invoice["meta"][key] = arrow.get(invoice["meta"][key])

env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
rendered = env.get_template("template.html").render(
    meta=invoice["meta"],
    items=invoice["items"],
    total=sum(item["total"] for item in invoice["items"]),
)

print(rendered)
