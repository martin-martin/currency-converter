# CLI Currency Converter

A lightweight command-line interface to calculate currency conversions for specific dates using Python 3 and exchange rate information from the [European Central Bank](https://www.ecb.europa.eu/home/html/index.en.html).

![Example conversion process GIF](convert.gif)

## Rationale

Helpful if you need to know how much a certain currency was worth in another currency at a specific date (e.g. for doing your taxes as a contractor who earns in different currencies), as well as quick conversions from the CLI.

## Usage

```
usage: convert [-h] [-i input_currency] [-o output_currency] [-d date] amount

Convert between currencies at a specific date. Defaults to converting to Euro at today's date

positional arguments:
  amount                the amount to convert

options:
  -h, --help            show this help message and exit
  -i input_currency, --input input_currency
                        the original currency as 3-letter code. default: USD
  -o output_currency, --output output_currency
                        the output currency as 3-letter code. default: EUR
  -d date, --date date  the date to apply to the conversion in YYYY-MM-DD format. default: today
```

## Contribute

Contributions are very welcome. Please create an issue detailing your idea so I can take a look and comment on it before you do any work. Once we agree that it's a great idea that fits into this project, you an fork the code, add your feature, and create a PR. 

Here are some possible ideas that might be fun to implement:

- Improve documentation in README.md
- Connect `exchange-rates.py` so that dates out of range fetch new data from the web
- Add a list of currency abbreviations to `--help` menu
- Add option to use emojis as CLI flags (e.g. :calendar: instead of `-d`) 
- Expand the functionality (ideas welcome!)
