#!/usr/bin/env python
# coding: utf-8

# In[21]:


input_row = input('Введите ряд чисел через пробел:')
input_data = input_row.split(' ')
print_data = []

for item in input_data:  
    if input_data.count(item) > 1 and item not in print_data: 
        print_data.append(item)  

print(' '.join(sorted(print_data)))

