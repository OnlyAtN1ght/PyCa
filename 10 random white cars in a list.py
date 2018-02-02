dfW = pd.read_excel('White Cards.xlsx', sheet_name='Sheet1')
for i in range(0,10):
    scardW = dfW.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)
    cardW = scardW.iloc[0]['Content']
    cardsW.append(cardW)
   