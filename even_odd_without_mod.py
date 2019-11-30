def even_odd(n):
    return 'odd' if n&1 else 'even'


a = int(input('enter the number '))
res = even_odd(a)
print(res)
