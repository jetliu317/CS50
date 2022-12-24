# Bitcoin Index
import sys
import requests
import json

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print('Command-line argument is not a number')
        sys.exit(1)
else:
    print('Missing command-line argument')
    sys.exit(1)

try:
    index = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = index.json()
    bitcoin = response['bpi']['USD']['rate_float']
    total_amount = value * bitcoin
    print(f'${total_amount:,.4f}')
except (IndexError,requests.RequestException):
    print('Request Exception')
    sys.exit(1)
    
