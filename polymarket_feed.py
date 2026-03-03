import requests

def get_market_probability(market_id):

    url = f"https://gamma-api.polymarket.com/markets/{market_id}"
    r = requests.get(url)
    data = r.json()

    return float(data["outcomes"][0]["price"])
