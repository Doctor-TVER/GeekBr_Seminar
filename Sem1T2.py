'''Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.'''
lst =[1,2,3,5,4]
maxi = lst[0]
for i in range(1, len(lst)):
    if lst[i] > maxi:
        maxi = lst[i]
print(maxi)