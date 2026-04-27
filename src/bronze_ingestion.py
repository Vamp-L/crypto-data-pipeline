import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd"
}

response = requests.get(url, params=params)

data = response.json()

df = pd.DataFrame(data)

df.to_csv("data/Bronze/crypto_raw.csv", index=False)

print("Bronze Layer Saved")




