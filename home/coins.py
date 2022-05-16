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
        for x in coins:
            if x['symbol'] == 'BTC':
                price_btc = round(x['quote']['USD']['price'], 4)
                prices.append(price_btc)
            elif x['symbol'] == 'ETH':
                price_etf = round(x['quote']['USD']['price'], 4)
                prices.append(price_etf)
            elif x['symbol'] == 'XRP':
                price_xrp = round(x['quote']['USD']['price'], 4)
                prices.append(price_xrp)
            elif x['symbol'] == 'SOL':
                price_sol = round(x['quote']['USD']['price'], 4)
                prices.append(price_sol)
            elif x['symbol'] == 'DOGE':
                price_doge = round(x['quote']['USD']['price'], 4)
                prices.append(price_doge)
        return prices
