# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.append('ducati')

# # i = 0
# # while i < 4:
# #     print(f'\t{motorcycles[i]}')
# #     i += 1
# #n = len(motorcycles)
# for i in motorcycles: #range(n):
    
#     print(f'\t{i}')

# #motorcycles_1 = motorcycles.pop(2)
# # motorcycles_2 = motorcycles.remove('yamaha')
# #print(motorcycles_2)    
# motorcycles.sort(reverse = True)
# print(motorcycles)


# array = []
# for i in range(1234567):
#     array.append(i)
#     #    print(array[i])
# print(min(array))
# print(max(array))
# print(sum(array))

#print(array)


# squares = []
# for value in range(2, 11, 2):
#     square = 2 ** value
#     squares.append(square)
# print(squares)

# array = []
# res = 1
# for i in range(1, 11):
#     res *= 2
#     array.append(res)
# print(array)

# arr = [j ** 2 for j in range(1, 11)]
# print(arr)

# arr_3 = [k ** 3 for k in range(1, 11)]
# print(arr_3)
# print(arr_3[-2:])
# for i in arr_3[-3:]:
#     print(i)
# arr_copy = arr_3[:]
# arr_3.append('test')
# print(arr_3)
# print(arr_copy)
# print(arr_3[10])

# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])
# print(dimensions)
# dimensions = (400, 500)
# print(dimensions)

#list1 = []
#list_1 = list()
# list_1 = [1, 2, 3, 7]
# print(list_1)
# #print(list_1)

# # for i in list_1:
# #     print(i)
# # print(len(list_1))
# # print(list_1[3])

# # print(list_1)
# # list_1.append(11)
# # print(list_1)
# # list_1.append(86)
# # print(list_1)
# list_1.insert(2,23)
# print(list_1)

# list1 = []
# print(list1)
# for i in range(5):
#     list1.append(i)
#     print(list1)
# print(list1.pop())

# t = ()
# print(type(t))


# t = (1, 5, 3, 6)
# print(type(t))

# v= [1, 8 , 9]
# print(type(v))

# v = tuple(v)
# print(type(v))

# a, b, c = v
# print(a, b, c)

#Кортеж
# t = (1, 3, 5, 6)

# for i in range(len(t)):
#     print(t[i])
    
# t[0] = 2
# print(t)

#Словари

d = {}
# d = dict()

d['q'] = 'qwerty'
d['w'] = 'werty'
print(d['q'])
print(d.items())
for (k,v) in d.items():
    print(k,v)

# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('gray')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}

# c = a.copy()
# u = a.union(b)
# i = a.intersection(b)
# dl = a.difference(b)
# dr = u.difference(a)
# q =a.union(b).difference(a.difference(b))
# print(c)
# print(u)
# print(i)
# print(dl)
# print(dr)
# print(q)


# a = {1, 8, 6}
# b = frozenset(a)
# print(b)

# list_1 = [i for i in range(1, 101)]
# print(list_1)

# list_1 = [i for i in range(2, 101) if i % 2 == 0]
# print(list_1)

# list_1 = [i for i in range(2, 101, 2)]
# print(list_1)

# list_1 = [(i,i) for i in range(2, 101) if i % 2 == 0]
# print(list_1)

# import time
# p_start = time.time()
# list_1 = [2 ** i for i in range(2, 101)]
# print(list_1)
# p_stop = time.time()
# res = (p_stop - p_start) * 1000
# print(res)