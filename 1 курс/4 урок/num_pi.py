import math


def pi(x):
    return '{p:.{0}f}'.format(x, p=math.pi)


x1 = int(input('Введите число знаков после запятой: '))
print(pi(x1))



