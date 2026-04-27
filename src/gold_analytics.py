import pandas as pd

df = pd.read_csv("data/Silver/crypto_clean.csv")

top_coin = df.sort_values("market_cap", ascending=False).head(15)

print(top_coin)

avg_price = df["current_price"].mean()

print(avg_price)

analytics = pd.DataFrame({
    "metric": ["avg_pprice"],
    "value": [avg_price]
})

print(analytics)

top_coin.to_csv("data/Gold/top_coin.csv", index=False)

analytics.to_csv("data/Gold/metrics.csv", index=False)

print("Gold Layer Saved")