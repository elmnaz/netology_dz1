#!/usr/bin/env python
# coding: utf-8

# In[35]:


month = input('Введите месяц рождения ').strip().lower()
day = int(input('Введите дату рождения '))

day_error_msg = 'Дата рождения введена некорректно'
if (day < 1):
    print(day_error_msg)
elif month == 'январь':
    if(day <21):
        print('Ваш знак зодиака: Козерог')
    elif(day>=21 and day<=31):
        print('Ваш знак зодиака: Водолей')
    else:
        print(day_error_msg)    
elif month == 'февраль':
    if(day <20):
        print('Ваш знак зодиака: Водолей')
    elif(day>=20 and day<=29):
        print('Ваш знак зодиака: Рыбы')
    else:
        print(day_error_msg)          
elif month == 'март':
    if(day <21):
        print('Ваш знак зодиака: Рыбы')
    elif(day>=21 and day<=31):
        print('Ваш знак зодиака: Овен')
    else:
        print(day_error_msg)          
elif month == 'апрель':
    if(day <21):
        print('Ваш знак зодиака: Овен')
    elif(day>=21 and day<=30):
        print('Ваш знак зодиака: Телец')
    else:
        print(day_error_msg)          
elif month == 'май':
    if(day <22):
        print('Ваш знак зодиака: Телец')
    elif(day>=22 and day<=31):
        print('Ваш знак зодиака: Близнецы')
    else:
        print(day_error_msg)          
elif month == 'июнь':
    if(day <22):
        print('Ваш знак зодиака: Близнецы')
    elif(day>=22 and day<=30):
        print('Ваш знак зодиака: Рак')
    else:
        print(day_error_msg)          
elif month == 'июль':
    if(day <23):
        print('Ваш знак зодиака: Рак')
    elif(day>=23 and day<=31):
        print('Ваш знак зодиака: Лев')
    else:
        print(day_error_msg)          
elif month == 'август':
    if(day <22):
        print('Ваш знак зодиака: Лев')
    elif(day>=22 and day<=31):
        print('Ваш знак зодиака: Дева')
    else:
        print(day_error_msg)          
elif month == 'сентябрь':
    if(day <24):
        print('Ваш знак зодиака: Дева')
    elif(day>=24 and day<=30):
        print('Ваш знак зодиака: Весы')
    else:
        print(day_error_msg)          
elif month == 'октябрь':
    if(day <24):
        print('Ваш знак зодиака: Весы')
    elif(day>=24 and day<=31):
        print('Ваш знак зодиака: Скорпион')
    else:
        print(day_error_msg)          
elif month == 'ноябрь':
    if(day <23):
        print('Ваш знак зодиака: Скорпион')
    elif(day>=23 and day<=30):
        print('Ваш знак зодиака: Стрелец')
    else:
        print(day_error_msg)          
elif month == 'декабрь':
    if(day <23):
        print('Ваш знак зодиака: Стрелец')
    elif(day>=23 and day<=31):
        print('Ваш знак зодиака: Козерог')
    else:
        print(day_error_msg)          
else:
    print('Месяц рождения введен некорректно')

