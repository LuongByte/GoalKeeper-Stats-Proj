import pandas as pd
import requests

keep = pd.read_html('https://fbref.com/en/comps/9/keepersadv/Premier-League-Stats', attrs = {"id":"stats_squads_keeper_adv_for"})

print(keep)

df = keep[0]
df.to_csv('keepers2021_data.csv', index=False)