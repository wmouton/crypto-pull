# https://coinmarketcap.com/api/documentation/v1/
# Import modules and API key
# import requests
from requests import Session
import secrets
from pprint import pprint as pp


class CPL:
    # https://coinmarketcap.com/api/documentation/v1/
    # https://coinmarketcap.com/api/documentation/v1/
    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token, }
        self.session = Session()
        self.session.headers.update(self.headers)

    def get_all_coins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        return data

    def get_price(self, symbol):
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
        parameters = {'symbol': symbol}
        r = self.session.get(url, params=parameters)
        data = r.json()['data']
        return data


cpl = CPL(secrets.API_KEY)


pp(cpl.get_all_coins())

pp(cpl.get_price('BTC'))
