#!/usr/bin/env python
# coding: utf-8

# In[59]:


import math
figure_type = input('Введите тип фигуры: круг, треугольник или прямоугольник:').strip().lower()

if figure_type == 'круг':
    try:
        radius = float(input('Введите радиус круга:'))
        square = round(math.pi*(radius**2),2)
    
        print('Площадь круга ', square)
    except ValueError:
        print('Ошибка при вводе числа')
elif figure_type == 'треугольник':
    try:
        side_a = float(input('Введите длину стороны A:'))
        side_b = float(input('Введите длину стороны B:'))
        side_c = float(input('Введите длину стороны C:'))

        # сумма длин двух любых сторон треугольника должна быть больше длины третьей стороны
        if(side_a+side_b <= side_c or side_c+side_b <= side_a or side_a+side_c <= side_b):
            print('Ошибка при вводе длин сторон треугольника')
        else:    
            p = (side_a+side_b+side_c)/2 # полупериметр треугольника
            square = round(math.sqrt(p*(p-side_a)*(p-side_b)*(p-side_c)),2)

            print('Площадь треугольника ', square)
    except ValueError:
        print('Ошибка при вводе числа')        
elif figure_type == 'прямоугольник':
    try:
        side_a = float(input('Введите длину стороны A:'))
        side_b = float(input('Введите длину стороны B:'))
        square = round(side_a*side_b,2)

        print('Площадь прямоугольника ', square)
    except ValueError:
        print('Ошибка при вводе числа')            
else: 
    print('Введен неверный тип фигуры')

