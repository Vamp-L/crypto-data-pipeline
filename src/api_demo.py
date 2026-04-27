import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd"
}

response = requests.get(url, params=params)

data = response.json()

df = pd.DataFrame(data)

print(df[["name", "symbol", "current_price", "market_cap"]])

df[["name", "symbol", "current_price", "market_cap"]].to_csv("data/crypto_prices.csv", index=False)


