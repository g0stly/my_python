your_code = int(input('Введите код города '))
your_minutes = int(input('Введите длительность переговоров '))


def call_tel(code, minutes):
    if code == 343:
        return 15 * minutes
    elif code == 381:
        return 18 * minutes
    elif code == 473:
        return 13 * minutes
    elif code == 485:
        return 11 * minutes


print(call_tel(your_code, your_minutes))
