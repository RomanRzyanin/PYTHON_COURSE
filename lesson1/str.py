x = {'a':1, 'b':2, 'c':3, 'd':4}
y = {'a':6, 'e':5, 'f':6}
print(x, y)
del x['d']
print(x)
z = x.setdefault('g', 7)
print(x)
x.update(y)
print(x)