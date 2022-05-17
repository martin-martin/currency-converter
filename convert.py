import argparse
import csv
from datetime import date


FILENAME = "USD-EUR.csv"

currency_parser = argparse.ArgumentParser(
    prog="convert",
    description="Convert between currencies at a specific date.\nDefaults to converting to Euro at today's date",
    epilog="Happy calculating 🧮",
)
currency_parser.add_argument(
    "amount", metavar="amount", type=float, help="the amount to convert"
)
currency_parser.add_argument(
    "-i",
    "--input",
    metavar="input_currency",
    type=str,
    default="USD",
    help="the original currency as 3-letter code. default: USD",
)
currency_parser.add_argument(
    "-o",
    "--output",
    metavar="output_currency",
    type=str,
    default="EUR",
    help="the output currency as 3-letter code. default: EUR",
)
currency_parser.add_argument(
    "-d",
    "--date",
    metavar="date",
    type=str,
    default=str(date.today()),
    help="the date to apply to the conversion in YYYY-MM-DD format. default: today",
)

args = currency_parser.parse_args()

rates = dict()

with open(FILENAME, "r") as csv_file:
    conversion_rates_reader = csv.DictReader(csv_file)
    for row in conversion_rates_reader:
        rates.update({row["date"]: float(row["rate_USD_EUR"])})


# calculate the new amount
rate_at_date = rates.get(args.date, None)
if rate_at_date:
    amount_converted = args.amount * rate_at_date
else:
    # TODO: run pipeline in exchange-rates.py to fetch fresh currency data
    raise NotImplementedError("Rate for specified date not available. Pulling fresh rates is not yet implemented.")
print(f"{amount_converted:.2f} {args.output} ({args.date})")