''' Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа. '''

# n = input().split('.')
# if len(n) > 1:
#     print(n[1][0])
# else:
#     print('нет')

# n = float(input())
# print(int(n % 1 * 10))

n = input('Введите число с плавающей точкой: ')
for i in range(len(n)):
    if n[i] == '.':
        print(n[i+1])
        break






