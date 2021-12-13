# Import modules and API key
import requests
import secrets

# https://coinmarketcap.com/api/documentation/v1/

# Test a request - basic
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': secrets.API_KEY,
}

r = requests.get(url, headers=headers)
# You can run 'r.status_code' to see the status code (you should get a 200'
# After you get a status code 200, run 'r.json()' to get back the data

# Build a class to easily make REST API calls
