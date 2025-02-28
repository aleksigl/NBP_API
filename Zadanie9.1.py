import requests
import csv


response = requests.get("https://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

rates = data[0]['rates']
currency_codes = [currency['code'] for currency in rates]
print(currency_codes)

with open('rates.csv', 'w', newline='') as csvfile:
    fieldnames = ['currency', 'code', 'bid', 'ask']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

    writer.writeheader()
    for entry in rates:
        writer.writerow({
            'currency': entry['currency'],
            'code': entry['code'],
            'bid': entry['bid'],
            'ask': entry['ask']
            })
