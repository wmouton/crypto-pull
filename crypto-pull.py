# https://coinmarketcap.com/api/documentation/v1/
# Import modules and API key
import requests
from requests import Session
import secrets

# Test a request - basic
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': secrets.API_KEY,
}

r = requests.get(url, headers=headers)


class CPL:
    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token, }
        self.session = Session()
        self.session.headers.update(headers=headers)


cpull = CPL(secrets.API_KEY)
