''' Вычислить число Пи c заданной точностью d
Пример:
    - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10 '''

from math import pi

d = input()
p = str(pi)[:len(d)]
print(p)

