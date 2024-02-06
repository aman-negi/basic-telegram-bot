import requests
import json

def get_stock_price(symbol):
    with open('credentials.json') as json_file:
        data = json.load(json_file)
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+str(symbol)+'&apikey='+str(data['alpha_api_token'])
        r = requests.get(url)
        data = r.json()
        return data['Global Quote']

