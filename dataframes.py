
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[94]:


dfB = pd.read_excel('Black Cards.xlsx', sheet_name='Sheet1')


# In[95]:


dfB.head()


# In[96]:


dfW = pd.read_excel('White Cards.xlsx', sheet_name='Sheet1')


# In[101]:


dfB.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)


# In[98]:


#dfW.head()


# In[102]:


sCardB = dfB.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)


# In[111]:


sCardB.tail()


# In[37]:


#CardB = sCardB.drop('Card Color', 1)


# In[115]:


sCardB.iloc[0]['Content']


# In[38]:


#CardB.head()


# In[46]:


#print(CardB.values,CardW.values)


# In[44]:


#sCardW = dfW.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)


# In[45]:


#CardW = sCardW.drop('Card Color', 1)


# In[55]:


#for ___ in cardsB[1] :
    sentence = card.replace('%%%', cardW[1])
    print(sentence)


# In[88]:


#"playedW[playedW['Content']==0].values[0]


# In[86]:


#playedW = CardW


# In[72]:


#print(dfW.iloc[529])


# In[87]:


#print(playedW)

