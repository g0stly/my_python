timetable = {
    "Пятница": {12: 250, 16: 350, 20: 450},
    "Чемпионы": {10: 250, 13: 350, 16: 350},
    "Пернатая банда": {10: 350, 14: 450, 18: 450}
}


def discount(date, tickets):
    if date == 'завтра':
        return 0.95
    if tickets >= 20:
        return 0.8
    else:
        return 1


your_film = input('Выбрать фильм: ')
your_date = input('Выбрать дату (сегодня, завтра): ')
your_time = input('Выбрать время: ')
your_tickets = input('Выбрать количество билетов: ')


if your_film and your_date and your_time and your_tickets:
    if your_film in timetable:
        if your_date == 'сегодня' or your_date == 'завтра':
            if int(your_time) in timetable[your_film]:
                print('Выбрали фильм:', your_film, '\nДень:', your_date, '\nВремя:', your_time,
                      '\nКоличество билетов:', your_tickets)
                print('Стоимость:', your_tickets * timetable[your_film][int(your_time)] * discount(your_date, int(your_tickets)), 'рублей')
            else:
                print('В это время сеансов нет.')
        else:
            print('На указанный день билеты не продаются.')
    else:
        print('Выбранный фильм не идет в прокате.')
else:
    print("Ошибка ввода.")
