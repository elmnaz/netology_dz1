#!/usr/bin/env python
# coding: utf-8

# In[33]:


width = 10
length = 205
height = 5

if(length > 200):
    print('Коробка для лыж')
elif (width <= 15 and length <= 15 and height <= 15):
    print('Коробка №1')
elif (width >15 and width<=50 or length>15 and length<=50 or height>15 and height<=50):
    print('Коробка №2')
else:
    print('Стандартная коробка №3')

