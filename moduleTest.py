import datetime
import requests

print(datetime.datetime.now())

resp = requests.get("https://api.bithumb.com/public/ticker/BTC")

print(resp.content)

