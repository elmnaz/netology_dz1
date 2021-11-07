#!/usr/bin/env python
# coding: utf-8

# In[44]:


number = 123321
num_to_str = str(number)

if len(num_to_str) == 6:
    if(int(num_to_str[0])+int(num_to_str[1])+int(num_to_str[2]) == int(num_to_str[3])+int(num_to_str[4])+int(num_to_str[5])):
        print('Cчастливый билет')
    else:
        print('Несчастливый билет')
else:
    print('Неверный номер билета')

