your_film = input('Выбрать фильм: ')
your_date = input('Выбрать дату (сегодня, завтра): ')
your_time = int(input('Выбрать время: '))
your_tickets = int(input('Выбрать количество билетов: ' ))


def cinema_price(film, time, tickets):
    if film == 'Пятница':
        if time == 12:
            return 250 * tickets
        if time == 16:
            return 350 * tickets
        if time == 20:
            return 450 * tickets
    if film == 'Чемпионы':
        if time == 10:
            return 250 * tickets
        if time == 13:
            return 350 * tickets
        if time == 16:
            return 350 * tickets
    if film == 'Пернатая банда':
        if time == 10:
            return 350 * tickets
        if time == 14:
            return 450 * tickets
        if time == 18:
            return 450 * tickets
    else:
        return 'Ошибка ввода'


def discount(date, tickets):
    if date == 'завтра':
        return 0.95
    if tickets >= 20:
        return 0.8
    else:
        return 1


print('Выбрали фильм:', your_film, 'День:', your_date, 'Время:', your_time,
      'Количество билетов:', your_tickets)

if type(cinema_price(your_film, your_time, your_tickets)) == int:
    print('Результат:', cinema_price(your_film, your_time, your_tickets) * discount(your_date, your_tickets), 'рублей')
else:
    print(cinema_price(your_film, your_time, your_tickets))
