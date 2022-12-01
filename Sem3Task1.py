'''Перемешать список чисел без модуля random'''
import time


def random_number(minimum=0, maximum=10):
    return int((time.time() % 1) * (maximum - minimum) + minimum)

lst = [1, 2, 5, 8, 8]
for i in range(len(lst)):
    j = random_number(0, len(lst)-1)
    lst[i], lst[j] = lst[j], lst[i]
print(lst)