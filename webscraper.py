import requests
import pandas as pd

res = requests.get('https://gol.gg/game/stats/25989/page-fullstats/')

df = pd.read_html(res.text, skiprows=[0])
df = pd.concat(df)
df.to_csv("data.csv", index=False)
print(df)
