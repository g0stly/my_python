a = input('Введите первое число: ')
b = input('Введите второе число: ')
c = input('Введите операцию: ')


def calculate(x, y, operator):
    try:
        if operator == '+':
            return x + y
        elif operator == '-':
            return x - y
        elif operator == '*':
            return x * y
        elif operator == '/':
            return x/y
        elif operator == '^':
            return x**y
    except ValueError:
        print('Ошибка входных данных.')
    except ZeroDivisionError:
        print('Ошибка деления на ноль.')


print('Результат:', calculate(int(a), int(b), c))
