'''Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.'''

#task1
# import random

# n = int(input('Введите количество монеток на столе n: '))
# moneys = []
# for i in range (n):
#     moneys.append(random.randint(0, 1))
# print(moneys)

# k = 0
# j = 0
# for money in moneys:
#     if money == 1:
#         k += 1
#     elif money == 0:
#         j += 1

# if k > j:
#     print(f'{j} монет необходимо перевернуть, чтобы все монеты лежали одной стороной')
# else:
#     print(f'{k} монет необходимо перевернуть, чтобы все монеты лежали одной стороной')    

'''Задача 12: 
Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.'''

import random
import time
import math as m

def Square(s, p):
    D = s ** 2 - 4 * p
    x_1 = int(abs((-s - m.sqrt(D))/2))
    x_2 = int(abs((-s + m.sqrt(D))/2))
    if x_1 < x_2:
        return x_1, x_2
    else:
        return x_2, x_1
    
first_digit = random.randint(1, 1000)
second_digit = random.randint(1, 1000)
product = first_digit * second_digit
sum = first_digit + second_digit
print(f'Петя загадал два натуральных числа {first_digit} и {second_digit}, произведение чисел a * b = {product}, сумма чисел a + b = {sum}. Угадай числа a и b')

pr_start = time.time()

print(Square(sum, product))
    
pr_stop = time.time()

# print(sum, product)
# print(first_digit, second_digit)

res = (pr_stop - pr_start) * 1000
print(res)
'''Задача 14: 
Требуется вывести все целые степени двойки (т.е. числа
вида 2k
), не превосходящие числа N.'''

#task3
# import time

# n = int(input('Введите натуральное число n: '))
# pr_st = time.time()
# squares = []
# for i in range(n):
#     square = 2 ** i
#     if square <= n:
#         squares.append(square)
        
#         #print(square)
#     else:
#         break
    
# print(f'Последовательность степеней двойки {squares} не превосходящих {n}.')

# pr_stop = time.time()        
# print((pr_stop - pr_st) * 1000)

# squares = [square ** 2 for square in range(n)]

# arr = [j ** 2 for j in range(1, 11)]

# x = 10 % 2
# y = 10 % 6
# print(x, y)

# list_1 = [2 ** i for i in range(n)]
# print(list_1)