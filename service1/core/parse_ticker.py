import requests
import json

from service1.models import CryptoCoins, ERC20Tokens

def get_current_price(crypto_name, type, coin_id):

    api_url = "https://api.coinmarketcap.com/v1/ticker/" + crypto_name

    r = requests.get(api_url)

    if r.status_code == 200:

        json_obj = json.loads(r.text)[0]

        if type == 'erc20':

            token = ERC20Tokens.objects.get(token_id=coin_id)
            token.current_price = json_obj['price_usd']
            token.save()

        if type == 'coin':

            coin = CryptoCoins.objects.get(coin_id=coin_id)
            coin.current_price = json_obj['price_usd']
            coin.save()

    return r.text