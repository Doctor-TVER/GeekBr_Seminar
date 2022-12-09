'''Найти НОД и НОК'''

def f(n):
    lst = []
    i = 2
    while n > 1:
        if n % i == 0:
            lst.append(i)
            n /= i
        else:
            i += 1
    return lst


n1, n2 = int(input()), int(input())

lst1 = set(f(n1))
lst2 = set(f(n2))

l = lst1.intersection(lst2)
nod = 1
for i in l:
    nod *= i
print(nod)
nok = int((n1 * n2) / nod)
print(nok)