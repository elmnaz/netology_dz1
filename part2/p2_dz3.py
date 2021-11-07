#!/usr/bin/env python
# coding: utf-8

# In[7]:


boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if(len(boys) != len(girls)):
    print('Внимание, кто-то может остаться без пары!')
else:
    pars = zip(sorted(boys), sorted(girls))
    
    print('Идеальные пары: ')
    for element in pars:
        print(f'{element[0]} и {element[1]}')