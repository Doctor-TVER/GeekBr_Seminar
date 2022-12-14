'''Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.'''

n = '1 - 2 * 3'
n = n.split()
while len(n) > 1:
    while '*' in n or '/' in n:
        if n.count('*') > 0 and n.count('/')> 0:
            if n.index('*') < n.index('/'):
                n[n.index('*')-1] = int(n[n.index('*')-1]) * int(n[n.index('*')+1])
                n.pop(n.index('*')+1)
                n.pop(n.index('*'))
            else:
                n[n.index('/')-1] = int(n[n.index('/')-1]) / int(n[n.index('/')+1])
                n.pop(n.index('/')+1)
                n.pop(n.index('/'))
        else:
            if '*' in n:
                n[n.index('*')-1] = int(n[n.index('*')-1]) * int(n[n.index('*')+1])
                n.pop(n.index('*')+1)
                n.pop(n.index('*'))
            else:
                n[n.index('/')-1] = int(n[n.index('/')-1]) / int(n[n.index('/')+1])
                n.pop(n.index('/')+1)
                n.pop(n.index('/'))
    while '+' in n or '-' in n:
        if n.count('+') > 0 and n.count('-')> 0:
            if n.index('+') < n.index('-'):
                n[n.index('+')-1] = int(n[n.index('+')-1]) + int(n[n.index('+')+1])
                n.pop(n.index('+')+1)
                n.pop(n.index('+'))
            else:
                n[n.index('-')-1] = int(n[n.index('-')-1]) - int(n[n.index('-')+1])
                n.pop(n.index('-')+1)
                n.pop(n.index('-'))
        else:
            if '+' in n:
                n[n.index('+')-1] = int(n[n.index('+')-1]) + int(n[n.index('+')+1])
                n.pop(n.index('+')+1)
                n.pop(n.index('+'))
            else:
                n[n.index('-')-1] = int(n[n.index('-')-1]) - int(n[n.index('-')+1])
                n.pop(n.index('-')+1)
                n.pop(n.index('-'))
print(n)


