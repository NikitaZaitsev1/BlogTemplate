import requests


class Coins:
    def get_coins(self):
        prices = []
        headers = {
            'X-CMC_PRO_API_KEY': 'b712a699-6b41-4381-9250-d03f42caa1c9',
            'Accepts': 'application/json'
        }

        params = {
            'start': '1',
            'limit': '10',
            'convert': 'USD'
        }

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

        coins_json = requests.get(url, params=params, headers=headers).json()

        coins = coins_json['data']
        # while True:
        for coin in coins:
            if coin['symbol'] == 'BTC':
                price_btc = round(coin['quote']['USD']['price'], 2)
                prices.append(price_btc)
            elif coin['symbol'] == 'ETH':
                price_etf = round(coin['quote']['USD']['price'], 2)
                prices.append(price_etf)
            elif coin['symbol'] == 'XRP':
                price_xrp = round(coin['quote']['USD']['price'], 4)
                prices.append(price_xrp)
            elif coin['symbol'] == 'SOL':
                price_sol = round(coin['quote']['USD']['price'], 2)
                prices.append(price_sol)
            elif coin['symbol'] == 'DOGE':
                price_doge = round(coin['quote']['USD']['price'], 4)
                prices.append(price_doge)

        return prices
