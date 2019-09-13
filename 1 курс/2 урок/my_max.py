x1 = int(input('Введите первое число: '))
y1 = int(input('Введите второе число: '))


def maximal(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return 'Числа равны'


print(maximal(x1, y1))
