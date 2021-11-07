#!/usr/bin/env python
# coding: utf-8

# In[11]:


word = 'test'

if len(word)%2 == 1:
    st = len(word)//2
    print(word[st:st+1])
else:
    st = len(word)//2
    print(word[st-1:st+1])

