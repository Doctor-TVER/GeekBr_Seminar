'''Задана натуральная степень k. Сформировать случайным
образом список коэффициентов (значения от 0 до 100)* многочлена
и записать в файл многочлен степени k.
    *Пример:*
    - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
    -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0'''

import random

k = int(input())
n = [random.randint(-100, 100) for _ in range(k + 1)]
print(n)


def f(k, n):
    p = ''
    for i in range(k + 1):
        if k - i > 1 and n[i] != 0:
            p += f'{n[i]}*x^{k - i} + '
        elif k - i == 1 and n[i] != 0:
            p += f'{n[i]}*x + '
        elif n[i] == 0:
            p += ''
        elif n[i] == 1:
            p += 'x + '
        else:
            p += f'{n[i]} = 0'
    return p


with open('file.txt', 'w') as data:
    data.write(f(k, n).replace('+ -', '- '))



