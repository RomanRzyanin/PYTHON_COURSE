motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')

# i = 0
# while i < 4:
#     print(f'\t{motorcycles[i]}')
#     i += 1
n = len(motorcycles)
for i in range(n):
    
    print(f'\t{motorcycles[i]}')

#motorcycles_1 = motorcycles.pop(2)
# motorcycles_2 = motorcycles.remove('yamaha')
#print(motorcycles_2)    
motorcycles.sort(reverse = True)
print(motorcycles)
