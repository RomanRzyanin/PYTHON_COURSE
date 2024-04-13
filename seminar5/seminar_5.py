'''Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ..., где 
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
'''

# def fib(n):
#     if n <= 1:
#         return 1
#     return fib(n-1) + fib(n-2) 
# n = int(input('Введите число n = '))
# print(f'{n}-e число Фибоначчи = {fib(n)}') 

# n = int(input('Введите число n = '))
# for i in range(n):
#     print(fib(i), end = ' ')
# print(f'{n}-e число Фибоначчи = {fib1(n)}', end = ' ')         
'''Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''
# def bad_grade(list_1):
#     max1 = max(list_1)
#     min1 = min(list_1)
#     for i in range(len(list_1)):
#         if list_1[i] == max1:
#             list_1[i] = min1
#     return list_1

# list_1 = [1,3,4,5,4,3,2,1,2,5,5,5,5]
# print(list_1)
# print(bad_grade(list_1))

'''Задача №35. 
Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes '''

# def prime_number(n):
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n
# res = prime_number(11)
# if res == True:
#     print('Yes')
# else:
#     print('No')

# import os    
# def simple_number(number):
#     if number % 2 == 0:
#         return 'no'
#     for i in range(3, number//2, 2):
#         if number % i == 0:
#            return 'no'
#     return 'yes'
# #os.system('cls' if os.name == 'nt' else 'clear'))
# print(simple_number((2 ** 82589933) - 1))


# def simple_number(number, dev=2):
#     if number==dev:
#             #print('yes')
#             return 'yes'
#     if number%dev==0:
#             #print('no')
#             return 'no'
#     return simple_number(number, dev+1)
    

# print(simple_number(17))


'''Задача №37. 
Решение в группах
15 минут
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3'''

# def revers(n):
#     a = int(input('a = '))
#     if n == 1:
#         return print(a, end = ' ')
#     return print(revers(n-1) + a)
        
# revers(5)    

# def reverse_sequence(n):
#     if n == 0:
#         return
#     x = input('Введите элемент -> ')
#     reverse_sequence(n-1)
#     print(x, end=' ')
# n = int(input('Число элементов n = '))
# reverse_sequence(n)
    
# def funct(n):
#     a=input()
#     if n==1:
#         return a
#     return funct(n-1) + a

# n=int(input())
# print(funct(n))    


# def recr(n):
#     a=input()
#     if n==1:
#         return a
#     return recr(n-1)+a

# n=int(input())
# print(recr(n))
# import time
# import sys
# sys.setrecursionlimit(1002)
# def invest(n):
#     print(n)
#     if n == 1:
#         return 1
#     return invest(n - 1) * n
# sum = invest(5)
# print(sum)

import random
def revers_values(N):
    num = str(random.randint(1, 99))
    print(num)
    if N == 1:
        return num
    return revers_values(N-1) + f' {num}'
print(revers_values(2))