import config, csv, json
from binance.client import Client
from tafunc import srsi_analyze

#@todo: add overload for user selection of data intervals
#this function gets the kline data provided in the binance api
def get_klines():
    client = Client(config.API_KEY,config.API_SECRET)
    
    #get the possible exchanges for the quoting asset, that are spot tradeable
    exinfo = client.get_exchange_info()
    exlist = []

    for symbol in exinfo["symbols"]:
        if((symbol["quoteAsset"] == "USDT") & (symbol["permissions"].count("SPOT") == 1)):
            exlist.append(symbol["symbol"])

    #getting the kline data to analyse for the exchangeable assets
    klines = {}
    coin_dict = {}
    for exchange in exlist:
        candledata = []
        try:
            print(exchange)
            candledata.append(client.get_klines(symbol = exchange, interval = Client.KLINE_INTERVAL_4HOUR, limit = 100))
            klines[exchange] = candledata
            coin_dict[exchange] = srsi_analyze(candledata)
            print("done")
        except Exception as e:
            print("can't because")
            print(e)

    return (coin_dict)

