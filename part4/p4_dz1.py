#!/usr/bin/env python
# coding: utf-8

# In[10]:


import json
purchases = {}

f = open('purchase_log.txt', 'r')
for i, line in enumerate(f):
    if i> 0:
        dict_ = json.loads(line.strip())
        #print(dict_)
        purchases[dict_['user_id']] = dict_['category']    
    if i> 10: 
        break
print(purchases)


# In[25]:


import json
import random
f = open('visit_log.csv', 'r')
fw = open('funnel.csv', 'a')

for i, line in enumerate(f):
    if i> 0:
        category = random.randint(0,5)
        if category > 0:
            new_line = line.strip() + ',' + str(category) + '\n'
            fw.write(new_line)

