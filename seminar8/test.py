# last_name = input('Введите фамилию: ')
# first_name = input('Введите имя: ')
# phone_number = input('Введите номер телефона: ')
# arr = [last_name, first_name, phone_number]
# info = ' '.join(arr)
# print(info)


# file = 'phonebook.txt'
# table=[['Last_name', 'First_name', 'Phone_number']]
# with open(file, 'r', encoding='utf-8') as f:
#     print('Last_Name first_name phone')
#     for line in f:
#         table.append(line.split())
#     for row in table:
#         print('| {:<12} | {:<12} | {:<15} |'.format(*row))
      



        
# from tabulate import tabulate
# table = [[1, 2222, 30, 500], [4, 55, 6777, 1]]
# print(tabulate(table))        
        
# import pandas as pd
# table = [[1, 2222, 30, 500], [4, 55, 6777, 1]]
# df = pd.DataFrame(table, columns = ['a', 'b', 'c', 'd'], index=['row_1', 'row_2'])
# print(df)

# table = [[1, 2222, 30, 500], [4, 55, 6777, 1]]
# for row in table:
#     print('| {:1} | {:^10} | {:>4} | {:<3} |'.format(*row))
    
    
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
# print(line)
# data.close()


# with open('file.txt', 'w') as data:
#     data.write('test_1\n')
#     data.write('test_2\n')


# import datetime

# def print_time():
#     now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
#     # now = datetime.now()
#     # current_time = now.strftime("%H:%M")
#     print("Current Time:", now)

# print_time()

# print(Ellipsis)
# print(...)
# print(...)

# title = "The walrus operator"
# #words_count = len(title.split())
# print(title)
# words_count = len(title.split())
# print(words_count)
# if words_count > 10:
#     print("Too many words in paragraph title:", words_count)
# else:
#     print("Paragraph title is suitable. Words count:", words_count)
    
# def get_words_count(s):
#     # Your code here
#     if s == "":
#         return 0
       
#     count = 0
    
#     for c in s:
#         if c == "_":
#             count += 1

#     return count + 1

# def get_words_count_1(s):
#     res = len(s.split('_')) if s != '' else 0
#     return res
# s = 'fsb_terb_reba_rebv'
# print(get_words_count(s))
# print(get_words_count_1(s))



# for letter in s:
#     if letter == "y":
#         break

#     print(letter, end = '')
# else:
#     print("There is no letter 'y' in string")



# s = "IF the implementation is hard to explain, it's a bad idea."    
# def print_letters(s):
#     for c in s:
#         if c.isupper():
#             print(c)
#         elif c == ' ':
#             break
#     else:
#         print('no spaces')
# print_letters(s)

# print('Java')
# print('Ruby')
# print('Scala')
# print('Python', end='+')  # print('C++')
# # print('GO')
# print('C#', end='=')  # print('C')
# print('awesome')
# # finish

# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')

# n = int(input())
# print(-(-n // 4))

p_1, p_2 = inpit(), input()
if p_1 == p_2:
    print('Пароль принят')
else:
    print('Пароль не принят')