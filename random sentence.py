
# coding: utf-8

# In[162]:


import pandas as pd
import numpy as np


# In[163]:


dfB = pd.read_excel('Black Cards.xlsx', sheet_name='Sheet1')


# In[164]:


dfB.head()


# In[165]:


dfW = pd.read_excel('White Cards.xlsx', sheet_name='Sheet1')


# In[166]:


dfB.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)


# In[167]:


#dfW.head()


# In[168]:


scardB = dfB.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)


# In[169]:


scardB.tail()


# In[170]:


#CardB = sCardB.drop('Card Color', 1)


# In[171]:


cardB = scardB.iloc[0]['Content']


# In[172]:


#CardB.head()


# In[173]:


#print(CardB.values,CardW.values)


# In[174]:


scardW = dfW.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)


# In[175]:


cardW = scardW.iloc[0]['Content']


# In[176]:


#cardW = scardW.drop('Card Color', 1)


# In[177]:


#for ___ in cardsB[1] :
    sentence = card.replace('%%%', cardW[1])
    print(sentence)


# In[178]:


#"playedW[playedW['Content']==0].values[0]


# In[179]:


#playedW = cardW


# In[180]:


#print(dfW.iloc[529])


# In[181]:


#print(playedW)


# In[182]:


print(cardB,cardW)


# In[183]:


cardD = cardB.replace('___',cardW)


# In[184]:


print(cardD)

