# def sum_numbers(n, y = 'Hello'):
#     print(y)
#     sum = 0
#     for i in range(1, n+1):
#         sum += i 
        
#     return sum
    
# a = sum_numbers(5, 'qwerty')    
# print(a)

def sum_str(*args):
    
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'r', 't', 'p'))
print(sum_str(1, 3, 7, 8))