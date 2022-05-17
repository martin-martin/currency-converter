from lxml import etree  # Doesn't work on ARM (M1 Macs)
from urllib.request import urlopen
import csv


URL = "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/usd.xml"

with urlopen(URL) as response:
    with open("new-usd-eur-conversion-rate.xml", "wb") as xml_file:
        xml_file.write(response.read())


with open("new-usd-eur-conversion-rate.xml", "rb") as xml_file:
    tree = etree.parse(xml_file)


rates = tree.findall(".//{http://www.ecb.europa.eu/vocabulary/stats/exr/1}Obs")

conversion_dicts = [{"date": r.get("TIME_PERIOD"), "rate_USD_EUR": r.get("OBS_VALUE")} for r in rates]

with open('USD-EUR.csv', 'w') as csvfile:
    fieldnames = ['date', 'rate_USD_EUR']
    conversion_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    conversion_writer.writeheader()
    for row in conversion_dicts:
        conversion_writer.writerow(row)
