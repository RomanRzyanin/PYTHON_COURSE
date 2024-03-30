# seminar1

# task1
# n = int(input('Введите расстояние которое автомобиль проходит за сутки: '))
# m = int(input('Введите расстояние между городами: '))
# t = m // n + (m % n > 1)
# print(f'Количество дней затраченное на перемещение = {t}')



#task2
# first_class = int(input('Введите количество учеников в 1 классе: '))
# second_class = int(input('Введите количество учеников в 2 классе: '))
# third_class = int(input('Введите количество учеников в 3 классе: '))
# res = (first_class // 2 + first_class % 2) + (second_class // 2 + second_class % 2) + (third_class // 2 + third_class % 2)
# print(f'Общее количество парт = {res}')

#task3

# i = int(input('Введите вагон указаный в билете: '))
# j = int(input('Введите вагон в который сел Витя: '))
# if i == j:
#     print('Витя лошара')
# else:
#     res = i + j - 1
#     print(f'Всего вагонов {res}')




list_1 = [5, 2, 3, 4, 5]
print(list_1)
# list_2 = [1]
list_1 = list_1.append(5)

x = len(list_1)
list_1[x:] = 5
list_1[:0] = 2
print(list_1)
# max_b = 0

# for i in range(1, len(list_1) - 1):
#     max1 = list_1[i - 1] + list_1[i] + list_1[i + 1]
#     if max1 > max_b:
#         max_b = max1
# print(max_b)














