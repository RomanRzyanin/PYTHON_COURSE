# import math as m
# x = 2.465
# print(m.floor(x))
# print(m.ceil(x))

# a = float(input ("a = " ))
# if a <= 0 :
#     print ("Длина должна быть положительной")
# else:
#     p = 4 * a
#     s = a * a
# print ("p = ", p, "s = ", s )

# print(round(4.999, 2))

# '''Ракета запускается с точки на экваторе и развивает скорость v км/с. Каков
# результат запуска?
# Указание: если v < 7.8 км/с, то ракета упадет на Землю (вывести 0), если 7.8 <v
# <11.2, то ракета станет спутником Земли (вывести 1), если 11.2 < v < 16.4 , то ракета
#  станет спутником Солнца (вывести 2), если v > 16.4, то ракета покинет Солнечную
# Систему (вывести 3).
# Если будет введено значение, меньшее или равное 0, то вывести "error".'''


# v = float(input('Введите скорость ракету v (км/с) = '))
# if v <= 0:
#     print('Error')
# elif v < 7.8:
#     print('Ваша ракета упадет на землю')
# elif v < 11.2:
#     print('Ваша ракета станет спутником Земли')
# elif v < 16.4:
#     print('Ваша ракета станет спутником Солнца')
# else:
#     print('Ваша ракета покинет Солнечную Систему')


#print(round(25 * 1.83 ** 2, 2))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in numbers:
#     if number == 1:
#         print(f'{number}st')
#     elif number == 2:
#         print(f'{number}nd')
#     else:
#         print(f'{number}th')

# s = 1022
# p = 144157
# x, y = 0, 0

# # for x in range(1000):
# #     for y in range(1000):
# #         if x
       
# for x in range(1000):
#     y = s - x
#     if x * y == p and x <= y:
#         print(x, y)
        
        
import time
import random
x = random.randint(1, 1000)
y = random.randint(1, 1000)
s = x + y
p = x * y
print(s, p)
prg1_start = time.time()
# Введите ваше решение ниже

x, y = 0, 0

for x in range(s):
    y = s - x
    if x > y:
        break
    if x * y == p and x <= y:
        print(x, y)
        break

prg1_stop = time.time()

prg2_start = time.time()

x, y = 0, 0

for y in range(1000):
    for x in range(1000):
        if x > y:
            break
        if x + y == s and x * y == p:
            print(x, y)

prg2_stop = time.time()

res1 = (prg1_stop - prg1_start) * 1000
res2 = (prg2_stop - prg2_start) * 1000

print(res1)
print(res2)
        

        
