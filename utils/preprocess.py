#!/usr/bin/env python
# coding: utf-8

# In[4]:


import unicodedata


# In[5]:


def _removes_nonascii(tokens):
    def _removes(token):
        token = unicodedata.normalize('NFKD', token)
        return token.encode('ascii', 'ignore').decode('utf-8', 'ignore')
    
    return [_removes(_) for _ in tokens]

