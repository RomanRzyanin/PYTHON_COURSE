'''Задача №47. 
Решение в группах
У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values.

Задача №47. Решение в группах
Ввод:
values = [1, 23, 42, ‘asdfg’]
transformed_values = list(map(trasformation, values))
if values == transformed_values:
 print(‘ok’)
else:
 print(‘fail’)
Вывод:
ok
'''

# transformation = lambda x: x * x

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список

# transformed_values = list(map(transformation, values))

# if values != transformed_values:
# 	print('ok')
# else:
# 	print('fail')
 
# print(values)
# print(transformed_values)


'''Задача №49. Решение в группах
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна
Пример ввода и вывода данных представлены на
следующем слайде

Задача №49. Решение в группах
Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10
'''
# from math import pi


# def find_farthest_orbit(orbits):
#     s_orbits = list(map(lambda x: x[0]*x[1]*pi if x[0]!=x[1] else 0, orbits))
#     max_indx = s_orbits.index(max(s_orbits))
#     return orbits[max_indx]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (100, 100)]
# print(*find_farthest_orbit(orbits))


'''Задача №51. Решение в группах
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
Ввод: Вывод:
values = [0, 2, 10, 6] same
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)

'''
# values = [0, 2, 10, 6]
# same_by = list(filter(lambda a: True if a % 2 == 0 else False, values))
# if len(values) == len(same_by):
#     print('same')
# else:
#     print('different')

# values = [3, 5, 1]
# #same_by = list(filter(lambda a: True if a % 2 == 1 else False, values))
# if same_by(lambda x: True if x % 2 == 1 else False, values):
#     print('same')
# else:
#     print('different')

# import random   
# numbers = [random.randint(1,100) for i in range(5)]

# print(*numbers)

# is_odd = lambda number: True if number%2 else False

# odd_numbers = list(filter(is_odd, numbers))

# print(*odd_numbers)

# def same_by(characteristic, objects):
#     # Проверяем на пустой список
#     if not objects:
#         return True

#     # Вычисляем характеристики для всех объектов
#     characteristics = [characteristic(obj) for obj in objects]

#     # Проверяем на одинаковость характеристик
#     return len(set(characteristics)) == 1


# # Список объектов
# objects = [2, 4, 6, 8]

# # Вызываем функцию и выводим результат
# print(same_by(lambda x: x % 2, objects))


def same_by(charac, objects):
    return len(set(map(charac, objects))) in [0, 1]
values = [0, 2, 10, 5] 
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')









































'''Задача №49. Решение в группах
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна
Пример ввода и вывода данных представлены на
следующем слайде

Задача №49. Решение в группах
Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10
'''

# from math import pi

# def find_farthest_orbit(orbits):
#     s_orbits = list(map(lambda x: x[0]*x[1]*pi if x[0]!=x[1] else 0, orbits))
#     max_indx = s_orbits.index(max(s_orbits))
#     return orbits[max_indx]

# orbits = orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (100, 100)]
# print(find_farthest_orbit(orbits))

# from math import pi


# def find_farthest_orbit(orbits):
#     s_orbits = list(map(lambda x: x[0]*x[1]*pi if x[0]!=x[1] else 0, orbits))
#     max_indx = s_orbits.index(max(s_orbits))
#     return orbits[max_indx]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (100, 100)]
# print(*find_farthest_orbit(orbits))

# from math import pi

# def find_farthest_orbit(orb):
#     return max(orb, key = lambda x: pi * x[0] * x[1] if x[0] != x[1] else 0)

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))