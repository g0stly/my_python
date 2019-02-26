def func(s, x):
    if str.__len__(s) > x:
        return str.upper(s)
    else:
        return str.lower(s)


s1 = input('Введите строку: ')
x1 = int(input('Введите число x: '))
print(func(s1, x1))
