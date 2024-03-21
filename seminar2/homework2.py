'''Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.'''

#task1
import random

n = int(input('Введите количество монеток на столе n: '))
moneys = []
for i in range (n):
    moneys.append(random.randint(0, 1))
print(moneys)

k = 0
j = 0
for money in moneys:
    if money == 1:
        k += 1
    elif money == 0:
        j += 1

if k > j:
    print(f'{j} монет необходимо перевернуть, чтобы все монеты лежали одной стороной')
else:
    print(f'{k} монет необходимо перевернуть, чтобы все монеты лежали одной стороной')    

'''Задача 12: 
Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.'''

# import random
# import math as m
# first_digit = random.randint(1, 1000)
# second_digit = random.randint(1, 1000)
# product = first_digit * second_digit
# sum = first_digit + second_digit
# print(f'Петя загадал два натуральных числа {first_digit} и {second_digit}, произведение чисел a * b = {product}, сумма чисел a + b = {sum}. Угадай числа a и b')

# D = sum ** 2 - 4 * product
# x_1 = int((-sum - m.sqrt(D))/2)
# x_2 = int((-sum + m.sqrt(D))/2)

# if x_1 < 0:
#     print(f'Первое число = {-x_1}')
# else:
#     print(f'Первое число = {x_1}')
    
# if x_2 < 0:
#     print(f'Первое число = {-x_2}')
# else:
#     print(f'А второе число = {x_2}')   
  
#print(x_1, x_2)
#print(sum, product)
#print(first_digit, second_digit)

'''Задача 14: 
Требуется вывести все целые степени двойки (т.е. числа
вида 2k
), не превосходящие числа N.'''

# #task3

# n = int(input('Введите натуральное число n: '))
# squares = []
# for i in range(1, n):
#     square = 2 ** i
#     if square < n:
#         squares.append(square)
        
# print(f'Последовательность степеней двойки {squares} не превосходящих {n}.')

#squares = [square ** 2 for square in range(n)]

# arr = [j ** 2 for j in range(1, 11)]

x = 10 % 2
y = 10 % 6
print(x, y)