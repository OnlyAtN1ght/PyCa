import pandas as pd

dfB = pd.read_excel('Black Cards.xlsx', sheet_name='Sheet1')
scardB = dfB.sample()
cardB = scardB.iloc[0]['Content']
