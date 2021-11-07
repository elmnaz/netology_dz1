#!/usr/bin/env python
# coding: utf-8

# In[2]:


countries_temperature = [
['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
['Germany', [57.2, 55.4, 59, 59, 53.6]],
['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

for element in countries_temperature:
    country, temp_list = element
    avr_f = sum(temp_list)/len(temp_list) #средняя температура по Фаренгейту
    avr_c = round((avr_f-32)*5/9,1) #перевод гр.Фаренгейта в гр.Цельсия
    print (f'{country} - {avr_c} C')    
