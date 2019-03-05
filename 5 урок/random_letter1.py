import random

L = ['самовар', 'весна', 'лето']

word = random.choice(L)
letter = random.choice(word)
x = word.index(letter)
k = [word[:x], word[x+1:]]
bl = True

print('?'.join(k))
while bl:
    userLetter = input('Введите букву: ')
    if userLetter == letter:
        print('Все верно! Загадываемое слово:', word)
        bl = False
    else:
        print('Увы! Попробуйте еще раз!')
