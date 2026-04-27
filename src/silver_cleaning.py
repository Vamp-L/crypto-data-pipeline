import pandas as pd

df = pd.read_csv("data/Bronze/crypto_raw.csv")

df = df[["name", "symbol", "market_cap", "current_price"]]

df = df.dropna()

df = df.drop_duplicates()

df.to_csv("data/Silver/crypto_clean.csv", index=False)

print("Silver Layer Saved")