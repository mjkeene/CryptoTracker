import requests
import json
import time
from datetime import datetime, timezone

def makeApiCall():

    apiKey = '02277a81e2a6c41db301fb9f892fcf3fd747dbda'
    url = 'https://api.nomics.com/v1/currencies/ticker?key={0}&ids=BTC,ETH&interval=1d,30d&convert=USD'.format(apiKey)
    result = requests.get(url)
    global jsonResult 
    jsonResult = json.loads(result.text)
    

def processDataAndBuildString():
    
    bitcoin = jsonResult[0]
    btc_price = '$' + '{:,}'.format(round(float(bitcoin['price']), 2))
    btc_1d_percent = str(float(bitcoin['1d']['price_change_pct'])*100)+'%'
    btc_1d_price_change = '$' + '{:,}'.format(round(float(bitcoin['1d']['price_change']), 2))
    btc_30d_percent = str(float(bitcoin['30d']['price_change_pct'])*100)+'%'
    btc_30d_price_change = '$' + '{:,}'.format(round(float(bitcoin['30d']['price_change']), 2))

    ethereum = jsonResult[1]
    eth_price = '$' + '{:,}'.format(round(float(ethereum['price']), 2))
    eth_1d_percent = str(float(ethereum['1d']['price_change_pct'])*100)+'%'
    eth_1d_price_change = '$' + '{:,}'.format(round(float(ethereum['1d']['price_change']), 2))
    eth_30d_percent = str(float(ethereum['30d']['price_change_pct'])*100)+'%'
    eth_30d_price_change = '$' + '{:,}'.format(round(float(ethereum['30d']['price_change']), 2))
    
    last_updated = bitcoin['price_timestamp']
    datetime_obj = datetime.strptime(
        last_updated, '%Y-%m-%dT%H:%M:%S%z')
    diff = datetime.now(timezone.utc) - datetime_obj
    minutes_since_update = round(diff.seconds / 60, 1)
    
    btcMsg = 'BTC price: {0}, BTC 1d change: {1}, {2}, BTC 30d change: {3}, {4}'.format(btc_price, btc_1d_price_change, btc_1d_percent, btc_30d_price_change, btc_30d_percent)
    ethMsg = 'ETH price: {0}, ETH 1d change: {1}, {2}, ETH 30d change: {3}, {4}'.format(eth_price, eth_1d_price_change, eth_1d_percent, eth_30d_price_change, eth_30d_percent)
    lastUpdateMsg = 'Last updated {0} minutes ago'.format(minutes_since_update)
    
    fullMsg = btcMsg + ' ' + ethMsg + ' ' + lastUpdateMsg + ' '
    print(fullMsg*10)
    