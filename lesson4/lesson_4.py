# def f(x):
#     return x * x
# a = f
# print(a(5))

# def calc1(a, b):
#     return a + b

# calc1 = lambda a,b: a+b

# def calc2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(calc1, 5, 45)

# list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
# list_2 = []
# for lst in list_1:
#     if lst % 2 == 0:
#         list_2.append((lst, lst**2))
        
# print(list_2)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, list_1)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)

# list_1 = [x for x in range(1, 20)]
# print(list_1)
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# str_1 = '1 2 3 4 5 6 7 8 9 0' #input('Введите числа через пробел:').split()
# print(str_1)
# list_1 = list(map(int, str_1.split()))
# print(list_1)

# data = [15, 65, 4, 175, 36]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
# #res = map(int, list_1)
# res = filter(lambda x: x % 2 == 0, list_1)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

'''function zip'''

# users = ['user1', 'user2', 'user3', 'user4']
# ids = [1, 2, 3, 4, 5]
# salary = [111, 222, 333, 444]
# data = list(zip(users, ids, salary))
# print(data)

'''function enumerate'''

# print(list(enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])))

'''file'''

# colors = ['red', 'green888', 'blue']
# data = open('file.txt', 'a', encoding='utf-8') #указываем режим в котором будем работать
# data.writelines(colors) #без разделителей
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 3\n')
# print(56)

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# import os

# print(os.getcwd())

from math import factorial
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(factorial, numbers)))