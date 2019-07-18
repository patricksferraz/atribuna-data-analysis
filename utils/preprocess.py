#!/usr/bin/env python
# coding: utf-8

# In[4]:


import unicodedata
import inflect


# In[5]:


def _all2ascii(tokens):
    def _removes(token):
        token = unicodedata.normalize('NFKD', token)
        return token.encode('ascii', 'ignore').decode('utf-8', 'ignore')

    return [_removes(_) for _ in tokens]


# In[ ]:


def _all2lower(tokens):
    return [_.lower() for _ in tokens]


# In[2]:


def _numbers2words(tokens):
    inf = inflect.engine()
    return [inf.number_to_words(_) if _.isdigit() else _ for _ in tokens]


# In[ ]:


def normalize(tokens):
    tokens = _all2ascii(tokens)
    tokens = _all2lower(tokens)
    return tokens

