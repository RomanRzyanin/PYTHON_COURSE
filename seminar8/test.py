# last_name = input('Введите фамилию: ')
# first_name = input('Введите имя: ')
# phone_number = input('Введите номер телефона: ')
# arr = [last_name, first_name, phone_number]
# info = ' '.join(arr)
# print(info)


file = 'phonebook.txt'
table=[['Last_name', 'First_name', 'Phone_number']]
with open(file, 'r', encoding='utf-8') as f:
    print('Last_Name first_name phone')
    for line in f:
        table.append(line.split())
    for row in table:
        print('| {:<12} | {:<12} | {:<15} |'.format(*row))
      



        
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
