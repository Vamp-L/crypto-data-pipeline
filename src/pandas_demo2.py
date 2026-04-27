import requests
import pandas as pd
import os

url = "https://api.github.com/search/repositories"

params = {
    "q": "stars:>50000",
    "sort": "starts",
    "order": "desc",
    "per_page": 100
}

response = requests.get(url, params=params)

data = response.json()

repos = data["items"]

df = pd.DataFrame(repos)

os.makedirs("data/Bronze", exist_ok=True)

df.to_csv("data/Bronze/github_raw.csv", index=False)

print("Bronze Data Saved")