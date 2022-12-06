'''Даны два файла, в каждом из которых находится запись многочлена.
 Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*'''

s1, s2 ='', ''


def open_file(f, s):
    with open(f, 'r') as file:
        for line in file:
            s = line
    return s


s_1 = open_file('file.txt', s1)[:-4].split(' + ')
s_2 = open_file('file1.txt', s2)[:-4].split(' + ')


def calc(list):
    dct = {}
    for i in range(len(list)):
        if list[i].count('x^'):
            dct[int(list[i].split('^')[1])] = int(list[i].split('*')[0])
        elif list[i].count('x'):
            dct[1] = int(list[i].split('*')[0])
        else:
            dct[1] = int(list[i])
    return dct


dct1 = calc(s_1)
dct2 = calc(s_2)
long_ind = 0
for k in dct1.keys():
    if long_ind < k:
        long_ind = k
for k in dct2.keys():
    if long_ind < k:
        long_ind = k

d = {}
for i in range(long_ind, -1, -1):
    if i in dct1:
        if i in dct2:
            d[i] = dct1[i] + dct2[i]
        else:
            d[i] = dct1[i]
    elif i in dct2:
        [i] = dct2[i]

lst =[]
for i in range(long_ind, -1, -1):
    if i in d:
        if i == 1:
            lst.append(str(d[i]) + '*x')
        elif i == 0:
            lst.append(str(d[i]))
        else:
            lst.append(str(d[i]) + '*x^' + str(i))

with open('file2.txt', 'w') as file:
    print(*lst, file=file, sep = ' + ', end=' = 0\n')











