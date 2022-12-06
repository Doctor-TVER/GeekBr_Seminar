'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
    - 45 -> 101101
    - 3 -> 11
    - 2 -> 10'''

# n = int(input())
# lst = []
# while n > 0:
#     lst.append(n%2)
#     n//=2
# print(*lst[::-1],sep='')


# def dec_to_bin(n):
#     s = ''
#     while n > 0:
#         s = f'{n%2}{s}'
#         n //= 2
#     return s


#через рекурсию
def dec_to_bin(n):
    return f'{dec_to_bin(n//2)}{n%2}' if n > 0 else ''

print(dec_to_bin(45))
