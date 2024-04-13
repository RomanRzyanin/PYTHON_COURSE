'''Задача 34:
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод:                                     Вывод:
пара-ра-рам рам-пам-папам па-ра-па-дам     Парам пам-пам'''

# def check_rhythm(list_1):
#     dict_char = ["а", "у", "о", "ы", "и", "э", "я",
#                  "ю", "ё", "е", "a", "e", "i", "o", "u", "y"]
#     qual_char = []

#     for i in range(len(list_1)):
#         qual_char.append(list(filter(lambda x: x in dict_char, list_1[i])))

#     if len(set((list(map(len, qual_char))))) != 1:
#         print("Пам парам")
#     else:
#         print("Парам пам-пам")


# str_1 = (input("Введите строку> ").split())
# check_rhythm(str_1)



# stroka = 'пара-ра-рам' #рам-пам-папам па-ра-па-дам'

# stroka = stroka.split()
# if len(stroka) <= 1:
#     print('Количество фраз должно быть больше одной!')
# else:
#     dict_char = ["а", "у", "о", "ы", "и", "э", "я",
#                  "ю", "ё", "е"]
#     qual_char = []

#     for i in range(len(stroka)):
#             qual_char.append(list(filter(lambda x: x in dict_char, stroka[i])))

#     if len(set((list(map(len, qual_char))))) != 1:
#         print("Пам парам")
#     else:
#         print("Парам пам-пам")


# '''Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод:                                             Вывод:
# print_operation_table(lambda x, y: x * y)         1 2 3 4 5 6
#                                                   2 4 6 8 10 12
#                                                   3 6 9 12 15 18
#                                                   4 8 12 16 20 24
#                                                   5 10 15 20 25 30
#                                                   6 12 18 24 30 36 '''
                                                  
                                                  
# def print_operation_table(operation, num_rows = 9, num_colunms = 9):
#     for i in range(1, num_rows + 1):
#         for j in range(1, num_colunms + 1):
#             print(i * j, end = '\t')
#         print()
# print_operation_table()

# def print_operation_table(operation, n = 6, m = 6):
#     if n <=2 or m <= 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!') 
#     else:
#         table = []
#         for i in range(1, n + 1):
#             line = []
#             for j in range(1, m + 1):
#                 line.append(operation(i,j))
#             table.append(line)
        
#         for rows in table:
#             print(*rows)

#     # print("Искомый элемент> ", operation(n,m))

# x, y = map(int, input("Введите 2 значения через пробел> ").split())
# print_operation_table(lambda x, y: x * y, x, y)


# one_line=list(map(lambda x: operation(x, number), begin_list))



import numpy
numbers = numpy.array(list(range(1,26)))
numbers = numbers.reshape((5,5))
print(numbers)