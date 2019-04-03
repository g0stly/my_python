def instructions():
    print('\nПростой todo: \n1. Добавить задачу. \n2. Вывести список задач. \n3. Выход.')


command = 0
todo = []

while command != 3:
    instructions()
    command = int(input('\nУкажите число: '))
    if command == 1:
        new = {}
        new['Задача'] = input('СФормулируйте задачу: ')
        new['Категория'] = input('Добавьте категорию к задаче: ')
        new['Время'] = input('Добавьте время к задаче: ')
        todo.append(new)
    if command == 2:
        print()
        for task in todo:
            for option in task:
                print(option, ':', task[option])


