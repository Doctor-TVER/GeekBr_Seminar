'''Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N'''
n = int(input())
num = [i for i in range(-abs(n), abs(n)+1)]
# for i in range(-n, n+1):
#     print(i, end=' ')
print(*num, sep=',')