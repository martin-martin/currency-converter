# CLI Currency Converter

A lightweight command-line interface to calculate currency conversions for specific dates using Python 3 and the [exchangeratesapi.io](https://exchangeratesapi.io/).

![Example conversion process GIF](convert.gif)

## Rationale

Helpful if you need to know how much a certain currency was worth in another currency at a specific date (e.g. for doing your taxes as a contractor who earns in different currencies), as well as quick conversions from the CLI.

## Usage

```
usage: convert [-h] [-o output_currency] [-d date] amount input_currency

Convert between currencies at a specific date. Defaults to converting to Euro at today's date

positional arguments:
  amount                the amount to convert
  input_currency        the original currency as 3-letter code

optional arguments:
  -h, --help            show this help message and exit
  -o output_currency, --output output_currency
                        the output currency as 3-letter code. default: EUR
  -d date, --date date  the date to apply to the conversion in YYYY-MM-DD
                        format. default: today
```
