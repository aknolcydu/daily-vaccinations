#install imported packages + pip install xlwt
import requests
import pandas as pd
import io
import numpy as np
response = requests.get("https://raw.githubusercontent.com/tarikkranda/pi_datasets/main/country_vaccination_stats.csv")
urldata=response.content
data=pd.read_csv(io.StringIO(urldata.decode('utf-8')))
data.to_excel("input.xls", index=False, sheet_name="Input")
countries=data.groupby(['country']).count().reset_index()
for item in countries['country']:
    country = data.loc[data['country'] == item]
    default_value=0
    for vacc_value in country['daily_vaccinations']:
        if pd.isna(vacc_value):
            continue
        elif default_value==0:
            default_value=vacc_value
        elif vacc_value<default_value:
            default_value=vacc_value
    data.loc[data['country'] == item] = data.loc[data['country'] == item].replace(np.nan, default_value)
data.to_excel("output.xls", index=False, sheet_name="Output")


