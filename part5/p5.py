#!/usr/bin/env python
# coding: utf-8

# In[43]:


from datetime import datetime

#Задание 1
print ('Задание 1')
date_string = 'Wednesday, October 2, 2002'
date_datetime = datetime.strptime(date_string, '%A, %B %d, %Y')
print(date_datetime)


date_string = 'Friday, 11.10.13'
date_datetime = datetime.strptime(date_string, '%A, %d.%m.%y')
print(date_datetime)

date_string = 'Thursday, 18 August 1977'
date_datetime = datetime.strptime(date_string, '%A, %d %B %Y')
print(date_datetime)

#Задание 2
print ('\nЗадание 2')
stream = ['2018-04-02', '2018-02-29', '2018-19-02']

for item in stream:    
    try:
        date_datetime = datetime.strptime(item, '%Y-%m-%d')
        print (f'Корректная дата: {item}')
    except:
        print('Ошибка в данных: {}'.format(item))
    
#Задание 3
print ('\nЗадание 3')
from datetime import timedelta
def date_range (date_begin, date_end):
    date_list = list()
    try:
        datebegin_datetime = datetime.strptime(date_begin, '%Y-%m-%d')
    except:
        return date_list
    
    try:
        dateend_datetime = datetime.strptime(date_end, '%Y-%m-%d')
    except:
        return date_list
        
    if (dateend_datetime > datebegin_datetime):
        cur_day = datebegin_datetime
        while cur_day <= dateend_datetime:            
            date_list.append(cur_day.strftime('%Y-%m-%d'))
            cur_day = cur_day + timedelta(days=1)
            
    return date_list
           
return_list = date_range('2021-01-01', '2021-01-10')
print (return_list)


# In[ ]:




