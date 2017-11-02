import requests
from bs4 import BeautifulSoup
import json

from service1.models import HistoricalBasketData, CryptoCoinsNew

def fetch_hist_data(data_url, coin_id):

    r = requests.get(data_url)

    bsObj = BeautifulSoup(r.text)

    table_array = bsObj.findAll('td')

    total_array_length = len(table_array)

    for i in range(0, total_array_length, 7):

        new_data_obj = HistoricalBasketData()

        new_data_obj.coin_id = CryptoCoinsNew.objects.get(coin_id=coin_id)
        new_data_obj.date = table_array[i].text
        new_data_obj.close = table_array[i+4].text
        new_data_obj.save()

fetch_list = ["https://coinmarketcap.com/currencies/ripple/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/litecoin/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/dash/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/bitcoin-cash/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/nem/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/monero/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/neo/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/ethereum-classic/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/iota/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/bitconnect/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/lisk/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/omisego/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/civic/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/qtum/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/vertcoin/historical-data/?start=20130428&end=20171101",
              "https://coinmarketcap.com/currencies/stratis/historical-data/?start=20130428&end=20171101"
              ]

counter = 1

for list in fetch_list:

    fetch_hist_data(list, str(counter))

    counter = counter + 1