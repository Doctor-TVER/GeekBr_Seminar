'''Реализуйте алгоритм нахождения рандомного числа.(Не используя библиотеки связанные с рандомом)'''

import time
import datetime


def random_number(minimum, maximum):
    # now = str(time.time())
    # rnd = float(now[::-1][:3:])/1000
    now = datetime.datetime.now().microsecond
    rnd = round(now/1000000)
    return minimum + rnd*(maximum-minimum)


print(random_number(0, 60))


