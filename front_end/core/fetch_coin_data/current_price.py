import requests
import json

from service1.models import CryptoCoinsNew

ROOT_URL = "https://api.coinmarketcap.com/v1/ticker/"

def fetch_current_price(coin_name, coin_id):

    data_url = ROOT_URL + coin_name + '/'

    r = requests.get(data_url)

    save_coin_price = CryptoCoinsNew.objects.get(coin_id=coin_id)

    save_coin_price.current_price_dollar = json.loads(r.text)[0]['price_usd']
    save_coin_price.save()

fetch_list = ["bitcoin","ethereum","ripple","litecoin","dash","bitcoin-cash","nem","monero","neo","ethereum-classic","iota","bitconnect","lisk","omisego","civic","qtum","vertcoin","stratis"]

counter = 1

for list in fetch_list:

    fetch_current_price(list, str(counter))

    counter = counter + 1