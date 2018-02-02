import pandas as pd
import numpy as np

dfB = pd.read_excel('Black Cards.xlsx', sheet_name='Sheet1')
dfB.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)
scardB = dfB.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)
cardB = scardB.iloc[0]['Content']
