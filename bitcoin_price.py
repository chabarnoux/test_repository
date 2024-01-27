import requests
import time

def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()
    return data["bpi"]["USD"]["rate"]

while True:
    bitcoin_price = get_bitcoin_price()
    print(f"Current Bitcoin Price: {bitcoin_price} USD")
    time.sleep(5)