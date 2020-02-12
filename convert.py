import argparse
import json
import os
import sys
import urllib.request


base_URL = "https://api.exchangeratesapi.io"

# set up argument parsing
my_parser = argparse.ArgumentParser(prog='convert',
                                    description='Convert between currencies at a specific date.\nDefaults to converting to Euro at today\'s date',
                                    epilog='Happy calculating 🧮')
# Add the arguments
my_parser.add_argument('Amount',
                       metavar='amount',
                       type=float,
                       help='the amount to convert')
my_parser.add_argument('InCurrency',
                       metavar='input_currency',
                       type=str,
                       help='the original currency as 3-letter code')
my_parser.add_argument('-o',
                       '--output',
                       metavar='output_currency',
                       type=str,
                       default='EUR',
                       help='the output currency as 3-letter code. default: EUR')
my_parser.add_argument('-d',
                       '--date',
                       metavar='date',
                       type=str,
                       default='latest',
                       help='the date to apply to the conversion in YYYY-MM-DD format. default: today')

args = my_parser.parse_args()

# fetch the conversion rate
url = f'{base_URL}/{args.date}?base={args.InCurrency}&symbols={args.output}'
r = urllib.request.urlopen(url)
data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))

# calculate the new amount
amount_converted = args.Amount * data['rates'][args.output]
print(f"{amount_converted:.2f} {args.output} ({data['date']})")
