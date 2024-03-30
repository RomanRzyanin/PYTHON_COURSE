#task9
# import time

# def factorial(x):
#     fact = 1
#     for i in range(x, 1, -1):
#         fact = fact * i
        
#     # while x > 1:
#     #     fact = fact * x
#     #     x -= 1
#     return fact
        
# n = int(input('Введите любое целое неотрицательное число: '))

# prog_start = time.time()
# print(f'Факториал числа {n} = {factorial(n)}')
# prog_stop = time.time()

# print((prog_stop - prog_start) * 1000)
#task11
 
# a = int(input('Введите любое целое неотрицательное число > 1: '))

# if a == 0:  print(1)

# else:

#     fib_prev, fib_next = 0, 1
#     n = 1

#     while fib_next <= a:

#         if fib_next == a:
#             print(n + 1)
#             break

#         # fib_prev, fib_next = fib_next, fib_prev + fib_next
#         temp = fib_next
#         fib_next = fib_prev + fib_next
#         fib_prev = temp
        
#         n += 1
#     else:  print(-1)
    
#task13
'''Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в
свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая
длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала
0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50'''


# import random
# n = int(input('Введите количество рассматриваемых дней N: \n'))
# temp = []
# for i in range (n):
#     x = random.randint(-50, 50)
#     temp.append(x)
# print(f'Среднесуточная температура в соответсвующий день: {temp}\n')

# t_count = 0
# t_max_count = 0
# #arr = []
# #m = len(temp)
# for i in range(n):
#     if temp[i] > 0:
#         t_count += 1
    
#     elif temp[i] <= 0 and t_max_count < t_count: 
#         t_max_count = t_count
#         t_count = 0
# print(t_max_count)

# # t_сount = 0
# # t_max_count = 0
# # for i in range(len(arr)):
# #     if arr[i] > t_max:
# #         t_max = arr[i]
        
# if t_max_count == 1:
#     print(f'Оттепель за период {n} дней, длилась {t_max_count} день')
           
# elif t_max_count == 2 or t_max_count == 3 or t_max_count == 4:       
#     print(f'Оттепель за период {n} дней, длилась {t_max_count} дня')
    
# else:
#     print(f'Оттепель за период {n} дней, длилась {t_max_count} дней')
    
    
#task 15

'''Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза'''

list_1 = [5, 3, 5, 6, 3, 9, 4, 2, 3]

good = list_1[0]
bad = list_1[0]

for i in range(0, len(list_1)):
    if list_1[i] > good:
        good = list_1[i]
    elif list_1[i] < bad:
        bad = list_1[i]
print(f'Watermelon for me: {good}')
print(f'Watermelon for bitch: {bad}')