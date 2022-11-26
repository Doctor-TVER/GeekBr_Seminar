'''Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число'''

with open('file.txt', 'w') as data:
    data.write('2\n')
    data.write('5\n')
    data.write('8\n')
n = int(input())
num = [i for i in range(-abs(n), abs(n)+1)]
total = 1
with open('file.txt', 'r') as data:
    for line in data:
        total *= num[int(line)]
print(total)
