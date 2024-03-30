'''Задача №25. 
Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
'''


# string = input('Введите строку: ').split()
# result = dict()
# for i in string:
#     if i in result.keys():
#         result[i] += 1
#         print(f'{i}_{result[i]}', end = ' ')
#     else:
#         result[i] = 1
#         print(i, end= " ")
# print()
# print(string)

# list_1 = 'a a a b c a a d c d d'
# input_list = list_1.split()

# a = ''
# dict_1 = {}
# for i in input_list:
#     a += i
#     if i in dict_1:
#         dict_1[i] += 1
#         a += f'_{dict_1[i]}'
#     else:
#         dict_1[i] = 0
#     a += ' '

# print(a)



# str1 = 'a a a b c a a d c d d'
# str1 = str1.split()

# a = ''
# #print(type(a))
# str1 = str1.split()
# print(str1)
# for i in str1:
#     count1 = a.count(i)
#     #print(count1)
#     if a.count(i) == 0:
#         a += i+' '
#     else:
#         a += i+'_'+str(count1)+' '
# print(a.strip())

# # string = input("Введите строку:").split()

# # result = dict()

# # for i in string:
# #     if i in result.keys():
# #         print(f'{i}_{result[i]}', end=" ")
# #         result[i] += 1
# #     else:
# #         print(i, end= " ")
# #         result[i] = 1


# string = input("Введите строку:").split()

# result = dict()
# new_result = ""
# for i in string:
#     if i in result.keys():
#         new_result += f"{i}_{result[i]}"
#         result[i] += 1
#     else:
#         new_result += i
#         result[i] = 1
#     new_result += " "
# print(new_result)



# string = input("Введите строку:").split()

# result = dict()
# new_result = []
# for i in string:
#     if i in result.keys():
#         new_result.append(f"{i}_{result[i]}")
#         result[i] += 1
#     else:
#         new_result.append(i)
#         result[i] = 1
    
# print(" ".join(new_result))



# string = input("Введите строку:").split()

# result = dict()
# new_result = []
# for i in string:
#     if i in result.keys():
#         new_result.append(f"{i}_{result[i]}")
#         result[i] += 1
#     else:
#         new_result.append(i)
#         result[i] = 1
    
# print(*new_result)



'''Задача №27. 
Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure. So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13
'''

# str_1 = '''She sells sea shells on the sea shore The shells that she sells are sea 
#     shells I'm sure. So if she sells sea shells on the sea shore I'm sure. that the shells are sea shore shells'''
# lst = str_1.lower().split()
# print(lst)
# print(len(set(lst)))


'''Задача №29. Решение в группах
Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.
Примечание: Программные коды на следующих
слайдах'''


# n = int(input())
# max_number = 1000
# while n != 0:
#    n = int(input())
#    if max_number > n:
#        max_number = n
# print(max_number)

# n = int(input())
# max_number = -1
# while n < 0:
#    n = int(input())
#    if max_number < n:
#        n = max_number
# print(n)

max = 0
while True:
    n = int(input('Введите число '))
    if n > max:
        max = n
    elif n == 0:
        print(max)
        break
    
# High = 0
# number = None
# while number != 0 :
#     number = int(input ("введите пол. число: "))
#     if number > High:
#         High = number
#     # if number==0:
#     #     break
# print (High)