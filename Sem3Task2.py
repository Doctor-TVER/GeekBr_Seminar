'''Найти число в списке строк'''

lst = ['blue', 'red', 'gre2n']
n = 2
flag = 'False'
for c in lst:
    if str(n) in c:
    # if c.count(str(n))
            flag = 'True'
            break
print(flag)
