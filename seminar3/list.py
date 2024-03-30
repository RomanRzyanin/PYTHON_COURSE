# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = x[-3:]
# del x[-3:]
# x[:0] = y
# print(x)
# z = ['q', 'w', 'e', 'r', 't', 'y']
# x.extend(z)
# print(x)

# list_1 = []
# for i in range(10):
#     list_1.insert(0, i)
# print(list_1)

# n = [1, 2, 3, 4, 5]
# k = 3
# arr = []
# for i in range(len(n)):
#     arr.append(n[(i + k) % len(n)])
# print(arr)


# str_1 = 'this is a test'
# #str_1 = str_1.split()
# print("-".join(str_1.split()))

# x = 'Mississippi'
# print(x.rfind('ss'))
# print(x)

a = "(name, date), \n"
print(a)
# print(a.strip("("))
print(a.strip("( ) , \n"))
print(a.strip("\n ) ( ,"))
# print(a.rstrip("a"))