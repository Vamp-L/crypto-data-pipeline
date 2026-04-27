import pandas as pd

df = pd.read_csv("data/crypto_prices.csv")

print(df.info())
print(df.columns)

print(df[["name", "symbol", "current_price", "market_cap"]])


