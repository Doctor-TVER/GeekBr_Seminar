'''Задайте список из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
Для n = 3:  {1: 2, 2: 2.25 , 3: 36.9}'''

n = int(input())

dct = {i: round((1 + (1 / i)) ** i, 2) for i in range(1,n+1)}
print(dct)