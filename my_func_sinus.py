from math import sin


def f(x):
    if 0.2 <= x <= 0.9:
        return sin(x)
    else:
        return 1


data = float(input('Введите вещественное число: '))
print('Значение функции f:', f(data))
