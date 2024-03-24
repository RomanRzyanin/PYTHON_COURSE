'''Задача №17. 
Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6'''
# import random

# def RandomMassiveSort(n):
#     list_1 = []
#     for i in range(n):
#         list_1.append(random.randint(-10, 10))
#     list_1.sort()
#     return list_1

# def CountDigits(list):
#     count = 1
#     for i in range(1, len(list)):
#         if list[i] != list[i - 1]:
#             count += 1
#     return count

# n = int(input('Please enter the size of the array, n = '))
# arr = RandomMassiveSort(n)
# print(arr)
# print(CountDigits(arr))


'''Задача №19. 
Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]'''

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_2 = []
# k = 5
# for i in range(len(list_1) - k):
#     list_2.append(list_1[i + k])
# for i in range(k):
#     list_2.append(list_1[i])
# print(list_2)

'''Задача №21. 
Решение в группах
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)
   
'''Задача №23. 
Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)'''

# list_1 = [0, -1, 5, 2, 3]

# cnt = 0
# k = list_1[0]
# for i in range(1, len(list_1)):
#         if list_1[i] > k:
#             cnt += 1
#         k = list_1[i]         
# print(cnt)
        
