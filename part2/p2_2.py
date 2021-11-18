#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Задание 1
# Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого пользователя (пример структуры данных приведен ниже). Вам необходимо написать программу, которая выведет на экран множество уникальных гео-меток всех пользователей.

# Пример работы программы:
# ids = {‘user1’: [213, 213, 213, 15, 213],
# ‘user2’: [54, 54, 119, 119, 119],
# ‘user3’: [213, 98, 98, 35]}
# Результат: {98, 35, 15, 213, 54, 119} */

ids = {'user1': [213, 213, 213, 15, 213],
'user2': [54, 54, 119, 119, 119],
'user3': [213, 98, 98, 35]}

e = set()
[e.update(item) for item in ids.values()]
print(e)


# In[19]:


# Задание 2
# Дана переменная, в которой хранится список поисковых запросов пользователя (пример структуры данных приведен ниже). Вам необходимо написать программу, которая выведет на экран распределение количества слов в запросах в требуемом виде.

# Пример работы программы:# ##  
# queries = [
# ‘смотреть сериалы онлайн’,
# ‘новости спорта’,
# ‘афиша кино’,
# ‘курс доллара’,
# ‘сериалы этим летом’,
# ‘курс по питону’,
# ‘сериалы про спорт’,
# ]
# Результат:
# Поисковых запросов, содержащих 2 слов(а): 42.86%
# Поисковых запросов, содержащих 3 слов(а): 57.14%
    
queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт',
]

q2 = 0
q3 = 0
for item in queries:    
    if len(item.split()) == 2:        
        q2 += 1
    else:
        q3 += 1
    
print(f'Поисковых запросов, содержащих 2 слов(а): {round(q2*100/len(queries),2)}%')
print(f'Поисковых запросов, содержащих 3 слов(а): {round(q3*100/len(queries),2)}%')
 


# In[21]:


# Задание 3
# Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам. Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: (revenue / cost - 1) * 100

# Пример работы программы:
# results = {
# ‘vk’: {‘revenue’: 103, ‘cost’: 98},
# ‘yandex’: {‘revenue’: 179, ‘cost’: 153},
# ‘facebook’: {‘revenue’: 103, ‘cost’: 110},
# ‘adwords’: {‘revenue’: 35, ‘cost’: 34},
# ‘twitter’: {‘revenue’: 11, ‘cost’: 24},
# }
# Результат:
# {‘adwords’: {‘ROI’: 2.94, ‘cost’: 34, ‘revenue’: 35},
# ‘facebook’: {‘ROI’: -6.36, ‘cost’: 110, ‘revenue’: 103},
# ‘twitter’: {‘ROI’: -54.17, ‘cost’: 24, ‘revenue’: 11},
# ‘vk’: {‘ROI’: 5.1, ‘cost’: 98, ‘revenue’: 103},
# ‘yandex’: {‘ROI’: 16.99, ‘cost’: 153, ‘revenue’: 179}}

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

for key, val in results.items():
    results[key]['ROI'] = round((val['revenue']/val['cost'] - 1)*100,2)
    results[key] = dict(sorted(results[key].items()))
    
print(dict(sorted(results.items())))


# In[22]:


# Задание 4
# Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж (пример структуры данных приведен ниже). Напишите программу, которая возвращает название канала с максимальным объемом продаж.

# Пример работы программы:
# stats = {‘facebook’: 55, ‘yandex’: 115, ‘vk’: 120, ‘google’: 99, ‘email’: 42, ‘ok’: 98}
# Результат: Максимальный объем продаж на рекламном канале: vk

stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

print('Максимальный объем продаж на рекламном канале:', sorted(stats, key=stats.get, reverse=True)[0])


# In[24]:


# Задание 5 (необязательно)
# Дан список произвольной длины. Необходимо написать код, который на основе исходного списка составит словарь такого уровня вложенности, какова длина исхондого списка.

# Примеры работы программы:
# my_list = [‘2018-01-01’, ‘yandex’, ‘cpc’, 100]
# Результат: {‘2018-01-01’: {‘yandex’: {‘cpc’: 100}}}
# my_list = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’]
# Результат: {‘a’: {‘b’: {‘c’: {‘d’: {‘e’: ‘f’}}}}}

# ------ Нет решения --------


# In[25]:


#Задание 6 (необязательно)
# Дана книга рецептов с информацией о том, сколько ингредиентов нужно для приготовления блюда в расчете на одну порцию (пример данных представлен ниже).
# Напишите программу, которая будет запрашивать у пользователя количество порций для приготовления этих блюд и отображать информацию о суммарном количестве требуемых ингредиентов в указанном виде.

cook_book = {
'салат': [
{'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
{'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
{'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
{'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
{'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
{'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
{'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
],
'пицца': [
{'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
{'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
{'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
{'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
{'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
{'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
],
'лимонад': [
{'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
{'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
{'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
{'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
]
}

cnt = int(input('Введите количество порций:'))
ingr_list = {}

for dish_name, dish in cook_book.items():
    for ingr in dish:
        ingr_list.setdefault(ingr['ingridient_name'], {})        
        #ingr_list[ingr['ingridient_name']].setdefault(ingr['measure'], cnt*int(ingr['quantity']))
        if ingr['measure'] in ingr_list[ingr['ingridient_name']]:
            ingr_list[ingr['ingridient_name']][ingr['measure']] += cnt*int(ingr['quantity'])
        else:
            ingr_list[ingr['ingridient_name']][ingr['measure']] = cnt*int(ingr['quantity'])

ingr = list()
for key, mm in ingr_list.items():
    for name, val in mm.items():
        print(f'{key.capitalize()}: {val} {name}')

