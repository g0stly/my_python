from random import randint

n = randint(1, 4)
print('Угадай число от 1 до 4.')
n1 = int(input('Введи число: '))

if n == n1:
    print('Победа.')
elif n1 < n:
    print('Ваше число меньше загаданного. Повторите еще раз!')
elif n1 > n:
    print('Ваше число больше загаданного. Повторите еще раз!')
