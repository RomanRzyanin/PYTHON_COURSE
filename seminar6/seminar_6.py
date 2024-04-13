'''Задача №39. 
Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод: Вывод:
7 3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1 (каждое число вводится с новой строки)'''

# def create_list(n):
#     list_1 = []
#     for i in range(n):
#         list_1.append(int(input(f'Введите {i + 1} элемент списка ')))
#     return list_1

# #n = int(input('Введите размер 1-го списка n = '))
# #m = int(input('Введите размер 2-го списка m = '))
# list_1 = create_list(int(input('Введите размер 1-го списка n = ')))
# list_2 = create_list(int(input('Введите размер 2-го списка m = ')))

# print(*list_1)
# print(*list_2)
# # list_1 = [3, 1, 3, 4, 2, 4, 12]
# # list_2 = [4, 15, 43, 1, 15, 1]
# res = []
# for lst1 in list_1:
#     if lst1 not in list_2:
#         res.append(lst1)
# print(*res)

# def create_arr(st1):
#     return [int(input(f"Введите {i+1} элемент: ")) for i in range(int(input(st1)))]


# arr1 = create_arr("Число элементов массива 1: ")
# arr2 = create_arr("Число элементов массива 2: ")

# for el in arr1:
#     if el not in arr2:
#         print(el, end=" ")
        
'''Задача №41. 
Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
'''

# list_1 = [3, 5, 3, 4, 6, 4, 12, 6]
# cnt = 0
# for i in range(1, len(list_1) - 1):
#     if list_1[i - 1] < list_1[i] > list_1[i + 1]:
#         cnt += 1
        
# print(cnt)

# import random

# def create_arr(length):
#     return [random.randint(0, 99) for _ in range(length)]

# def count(arr):
#     counter = 0
#     for i in range(1, len(arr) - 1):
#         if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
#             counter += 1
#     return counter

# def recurs(arr):
#     if len(arr) <= 2:
#         return 0
#     counter = 0
#     if arr[1] > arr[0] and arr[1] > arr[2]:
#         counter += 1
#     return counter + recurs(arr[1:])

# arr = create_arr(16)
# print(arr)
# print("С помощью рекурсии:", recurs(arr))
# print("С помощью цикла:", count(arr))

    
'''Задача №43.
Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:        Вывод:
1 2 3 2 3    2
'''
# list_1 = [3, 5, 3, 4, 6, 4, 12, 6]
# cnt = 0
# # list_1 = list(map(int, input().split()))
# # print(list_1)
# for i in range(len(list_1)):
#     for j in range(i+1, len(list_1)):
#         if list_1[i] == list_1[j]:
#             cnt += 1
            
# print(cnt)

# def count(arr):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] == arr[j]:
#                 count += 1
#     return count

# def recursive(numbers):
#     if len(numbers) <= 1:
#         return 0
#     first_num = numbers[0]
#     rest_nums = numbers[1:]
#     count = 0
#     for i in rest_nums:
#         if first_num == i:
#             count += 1
#     return count + recursive(rest_nums)

# arr = [1, 2, 3, 2, 2, 2, 2, 3, 3]
# print(recursive(arr))
# print(count(arr))

'''Задача №45. 
Решение в группах
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 10 ** 5
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод:        Вывод:
300         220 284
'''

k = int(input('k = '))
import time
start = time.time()
if k < pow(10, 5):
    for n in range(1, k):
        m = 0
        sum2 = 0
        for i in range(1, n//2+1):
            if n % i == 0:
                m += i
        for j in range(1, m//2+1):
            if m % j == 0:
                sum2 += j
        if sum2 == n and m > n:
            print(n, m)
else:
    print('Сам считай эту уйню')
stop = time.time()
print((stop - start) * 1000)

# # Функция для вычисления суммы делителей числа
# def sum_of_divisors(n):
#     divisors_sum = 1  # Начинаем с 1, так как 1 - это делитель любого числа
#     # Перебираем возможные делители от 2 до корня из n
#     for i in range(2, int(n**0.5) + 1):
#         # Если число делится на i без остатка, то i - делитель
#         if n % i == 0:
#             divisors_sum += i  # Добавляем i в сумму делителей
#             # Если n / i не равно i, то n / i - это еще один делитель
#             if n // i != i:
#                 divisors_sum += n // i  # Добавляем n / i в сумму делителей
#     return divisors_sum  # Возвращаем сумму делителей

# # Функция для поиска дружественных чисел до заданного числа k
# def find_friendly_numbers(k):
#     friendly_pairs = []  # Список для хранения пар дружественных чисел
#     # Перебираем все числа от 1 до k
#     for n in range(1, k+1):
#         m = sum_of_divisors(n)  # Вычисляем сумму делителей числа n
#         # Если m <= k, n != m и сумма делителей m равна n, то n и m - дружественные числа
#         if m <= k and n != m and sum_of_divisors(m) == n:
#             # Если пара (m, n) еще не в списке, добавляем ее
#             if (m, n) not in friendly_pairs:
#                 friendly_pairs.append((n, m))
#     # Выводим все найденные пары дружественных чисел
#     for pair in friendly_pairs:
#         print(pair[0], pair[1])

# # Запрашиваем у пользователя число k
# k = int(input("Введите число k: "))
# # Вызываем функцию для поиска дружественных чисел
# find_friendly_numbers(k)