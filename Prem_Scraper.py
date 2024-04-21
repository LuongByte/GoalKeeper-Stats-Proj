import pandas as pd
import requests

df = pd.read_html('https://fbref.com/en/comps/9/keepersadv/Premier-League-Stats', attrs = {"id":"stats_squads_keeper_adv_for"})
print(df)