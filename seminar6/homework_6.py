'''Задача 30: 
Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: 
an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''
# def f(a_1, d, n):
#     '''Возвращает список арифметический прогрессии'''
#     res = [None] * n
#     for i in range(n):
#         res[i] = (a_1 + i * d)
#     return res

# a_1 = int(input('Введите первый член арифметической прогресии а_1 = '))
# d = int(input('Введите разноть арифметической прогресии d = '))
# n = int(input('Введите количество элементов арифметической прогресии n = '))

# res = [a_1 + i * d for i in range(n)]

# #res = f(a_1, d, n)
# print(*res)

'''Задача 32: 
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''
def search_index_number(lst, a = -5, b = 5):
    arr = []
    for i in range(len(lst)):
        if a < lst[i] < b:
            arr.append(i)
    return arr

import random
n = int(input('Введите размер списка n = '))
a = int(input('Введите нижнюю границу диапазона a = '))
b = int(input('Введите верхнюю границу диапазона b = '))
lst = [random.randint(-20, 20) for i in range(n)]
print('Исходный список', *lst) 
lst_index = search_index_number(lst, a, b)
print('Список индексов элементов исходного списка', *lst_index, ', принадлежащих диапазону от', a, 'до', b)
