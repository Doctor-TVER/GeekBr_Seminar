'''Найти второе вхождение числа'''

lst = ['qwe','asd','zxc','qwe','ertqwe']
x = 'qwe'
counter = 0
index = -1
for i in range(len(lst)):
    if x == lst[i]:
        counter += 1
        if counter == 2:
            index = i
            break
print(index)