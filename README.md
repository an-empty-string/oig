# Overengineered Invoice Generator

Overengineered Invoice Generator (or just _oig_ for short) is a tool for
converting YAML files describing an invoice into nice HTML files that you can
print to PDF or make available to your customer in some other way.

## Setup

In a Python virtual environment or otherwise, install the dependencies listed in
`requirements.txt`. You can do this with `pip install -r requirements.txt`.

## Usage

First, define an invoice file like this:

```yaml
meta:
  customer: ACME Widgets Incorporated
  number: 01-100
  date: 2022-03-01
  start_date: 2022-02-01
  end_date: 2022-02-28

  payable_to: |
    Your Name Here
    123 Main St.
    New York, NY 10001

items:
  - date: 2022-02-10
    hours: 2
    rate: 60
    description: Designed extremely cool new widget

  - date: 2022-02-23
    hours: 5
    rate: 40
    description: Made a kind of boring widget
```

Save this file to any path you please. Then, pipe it to `oig.py`. The output
will be self-contained HTML:

`./oig.py < acme-february-invoice.yml > acme-february-invoice.html`
