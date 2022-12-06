'''Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
    - [2, 3, 4, 5, 6] => [12, 15, 16];
    - [2, 3, 5, 6] => [12, 15]'''

# lst = [2, 3, 5, 6]
# lst1 = []
# for i in range(len(lst)//2+1):
#     lst1.append(lst[i]*lst[len(lst)-1-i])
# print(lst1 if len(lst)%2 !=0 else lst1[:-1])


# вариант решения
def pare_multiply(lst):
    lst1 = []
    centr = len(lst)//2
    for i in range(0, centr):
        lst1.append(lst[i] * lst[-i-1])
    if len(lst) != 0:
        lst1.append(lst[centr] ** 2)
    return lst1


print(pare_multiply([2,3,4,5,6]))
