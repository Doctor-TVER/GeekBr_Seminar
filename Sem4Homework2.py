'''Задайте натуральное число N. Напишите программу,
которая составит список простых множителей числа N.'''

n = int(input())
lst = []
i = 2
while n > 2:
    if n % i == 0:
        lst.append(i)
        n /= i
    else:
        i += 1
print(lst)

