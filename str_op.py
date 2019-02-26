s = "У лукоморья 123 дуб зеленый 456"

print('Буква "я" стоит в строке на', s.find('я'), "позиции")

x1 = s.count('у')
if x1 % 10 != 0 and x1 % 10 != 1:
    print('Буква "у" встречается в строке', x1, 'раза')
else:
    print('Буква "у" встречается в строке', x1, 'раз')

if not(s.isalpha()):
    print(s.upper())

if s.__len__() > 4:
    print(s.lower())

print(s.replace(s[0], "О"))
