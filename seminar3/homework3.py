'''Задача 16: 
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
'''


import random
def CreatRandomMassive(n):
    list_1 = []
    for i in range(n):
        list_1.append(random.randint(0, 10))
    return list_1

def ElementCounter(list, x):
    cnt = 0
    for i in list:
        if i == x:
            cnt += 1
    return cnt

n = int(input('Please enter the size of the array, n = '))
m = int(input('Please enter the x = '))
arr = CreatRandomMassive(n)
print(arr)
print(f'The number {m} occurs {ElementCounter(arr, m)} times.')

'''Задача 18: 
Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
'''


import math as m
def CreatRandomMassive(n):
    list_1 = []
    for i in range(1, n + 1):
        list_1.append(i * 3)
    return list_1

def CountDigit(list, x):
    min = len(list) * 3
    val = None
    for i in list:
        if m.fabs(x - i) < min:
            min = m.fabs(x - i)
            val = i
    return val
    

n = int(input('Please enter the size of the array, n = '))
x = int(input('Please enter the x = '))
arr = CreatRandomMassive(n)
print(len(arr) * 3)
print(arr)
print(f' Число {x} близко по значению к элементу {CountDigit(arr, x)}')


'''Задача 20: 
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.
'''

# word = str.lower(input("Введите слово: "))
# result = 0
# dict1 = {
#     "a": 1, "e": 1, "i": 1, "o": 1, "o": 1, "u": 1, "l": 1, "n": 1, "s": 1, "t": 1, "r": 1,
#     "d": 2, "g": 2,
#     "b": 3, "c": 3, "m": 3, "p": 3,
#     "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
#     "k": 5,
#     "j": 8, "x": 8,
#     "q": 10, "z": 10,
#     "а": 1, "в": 1, "е": 1, "и": 1, "н": 1, "о": 1, "р": 1, "с": 1, "т": 1,
#     "д": 2, "к": 2, "л": 2, "м": 2, "п": 2, "у": 2,
#     "б": 3, "г": 3, "ё": 3, "ь": 3, "я": 3,
#     "й": 4, "ы": 4,
#     "ж": 5, "з": 5, "х": 5, "ц": 5, "ч": 5,
#     "ш": 8, "э": 8, "ю": 8,
#     "ф": 10, "щ": 10, "ъ": 10
# }

# for i in word:
#     result = result + dict1[i]
# print(f"Стоимость введеного слова '{word.upper()}' составляет: {result}")

'''dict'''
contacts = {"мама": 545234, "брат": 234653, "сестра": 234546}
for i in contacts:
    print(i)

for key in contacts.keys():
    print(key)

print(contacts.keys())

for number in contacts.values():
    print(number)


for cont, number in contacts.items():
    print(number, cont)