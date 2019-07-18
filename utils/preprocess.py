#!/usr/bin/env python
# coding: utf-8

# In[4]:


import unicodedata


# In[5]:


def _all2ascii(tokens):
    def _removes(token):
        token = unicodedata.normalize('NFKD', token)
        return token.encode('ascii', 'ignore').decode('utf-8', 'ignore')

    return [_removes(_) for _ in tokens]


# In[ ]:


def _all2lower(tokens):
    return [_.lower() for _ in tokens]


# In[ ]:


def normalize(tokens):
    tokens = _all2ascii(tokens)
    tokens = _all2lower(tokens)
    return tokens

