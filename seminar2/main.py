#task9

# def factorial(x):
#     fact = 1
#     while x > 1:
#         fact = fact * x
#         x -= 1
#     return fact
        
# n = int(input('Введите любое целое неотрицательное число: '))
# print(f'Факториал числа {n} = {factorial(n)}')

#task11
 
a = int(input('Введите любое целое неотрицательное число > 1: '))

if a == 0:  print(1)

else:

    fib_prev, fib_next = 0, 1
    n = 1

    while fib_next <= a:

        if fib_next == a:
            print(n + 1)
            break

        # fib_prev, fib_next = fib_next, fib_prev + fib_next
        temp = fib_next
        fib_next = fib_prev + fib_next
        fib_prev = temp
        
        n += 1
    else:  print(-1)
    
#task13
# import random
# n = int(input('Введите количество рассматриваемых дней N: \n'))
# temp = []
# for i in range (n):
#     x = random.randint(-50, 50)
#     temp.append(x)
# print(f'Среднесуточная температура в соответсвующий день: {temp}\n')

# j = 0
# arr = []
# #m = len(temp)
# for i in range(len(temp)):
#     if temp[i] > 0:
#         j += 1
    
#     elif temp[i] <= 0: 
#         arr.append(j)
#         j = 0
# print(arr)

# t_max = 0
# for i in range(len(arr)):
#     if arr[i] > t_max:
#         t_max = arr[i]
        
# if t_max == 1:
#     print(f'Оттепель за период {n} дней, длилась {t_max} день')
           
# elif t_max == 2 or t_max == 3 or t_max == 4:       
#     print(f'Оттепель за период {n} дней, длилась {t_max} дня')
    
# else:
#     print(f'Оттепель за период {n} дней, длилась {t_max} дней')