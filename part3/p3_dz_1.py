#!/usr/bin/env python
# coding: utf-8

# In[ ]:


documents = [
{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
{'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
{'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
'1': ['2207 876234', '11-2'],
'2': ['10006'],
'3': []
}


def get_name_by_docnum(doc_num):
    for item in documents:
        if item.get('number') == doc_num:
            return 'Владелец документа: ' + item.get('name')
    return 'Документ не найден в базе'

def get_shelf_by_docnum(doc_num):
    for item, val in directories.items():
        if doc_num in val:
            return item
    return 0

def documents_info():
    for item in documents:
        shelf = get_shelf_by_docnum (item.get('number'))
        print(f"№{item.get('number')}, тип: {item.get('type')}, владелец: {item.get('name')}, полка хранения: {shelf}")
          
def set_new_shelf(shelf_num):    
    if shelf_num in directories:
        print ('Такая полка уже существует. Текущий перечень полок: ', ','.join(directories.keys()))
    else:
        directories[shelf_num] = []
        print ('Полка добавлена. Текущий перечень полок: ', ','.join(directories.keys()))
    return directories

def delete_shelf(shelf_num):
    if shelf_num in directories:
        if len(directories[shelf_num]) == 0:
            del directories[shelf_num]
            print ('Полка удалена. Текущий перечень полок: ', ','.join(directories.keys()))
        else:
            print ('На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: ', ','.join(directories.keys()))
    else:        
        print ('Такой полки не существует. Текущий перечень полок: ', ','.join(directories.keys()))
    return directories
    
inp = ''
while inp != 'q':
    inp = input('Введите команду: ')
    if inp == 'p':
        doc_num = input('Введите номер документа: ')
        owner = get_name_by_docnum(doc_num)
        print(owner)
    elif inp == 's':
        doc_num = input('Введите номер документа: ')
        shelf_num = get_shelf_by_docnum(doc_num)
        if shelf_num == 0 :
            print ('Документ не найден в базе')
        else:
            print('Документ хранится на полке: ', shelf_num)
    elif inp == 'l':
        documents_info()
    elif inp == 'as':
        shelf_num = input('Введите номер полки: ')
        directories = set_new_shelf(shelf_num)        
    elif inp == 'ds':
        shelf_num = input('Введите номер полки: ')
        delete_shelf(shelf_num)
    else:
        print('Команда введена некорректно, повторите ввод')

