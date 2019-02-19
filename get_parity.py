x1 = int(input('Введите число '))


def even_test(x):
    if x % 2 == 0:
        return 'Число четно'
    else:
        return 'Число нечетно'


print(even_test(x1))
