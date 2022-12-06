''' Найдите корни квадратного уравнения Ax² + Bx + C = 0'''

# a, b, c = int(input()), int(input()), int(input())
s = '4 * x^2 - 4 * x + 1 = 0'
lst = s.split()
lst1 =[]
for i in lst:
    if i.isdigit() or i == '-':
        lst1.append(i)
    if i == '=':
        break
print(lst1)
i = 0
while lst1.count('-') != 0:
    if lst1[i] == '-':
        lst1[i] += lst1[i+1]
        lst1.pop(i+1)
        i = 0
    i += 1
for i in range(len(lst1)):
    lst1[i] = int(lst1[i])
print(lst1)
a, b, c = lst1

d = b ** 2 - 4 * a * c
if d < 0:
    print('нет корней')
elif d == 0:
    print(round(-b/(2*a),2))
else:
    print(round(-b + (d ** 0.5) / (2 * a),2))
    print(round(-b - (d ** 0.5) / (2 * a),2))
