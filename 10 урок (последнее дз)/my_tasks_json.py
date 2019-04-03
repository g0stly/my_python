def writer(filename, numbers):
    import json
    try:
        with open(filename, 'w') as f_obj:
            json.dump(numbers, f_obj)
    except Exception as e:
        print(e)


def reader(filename):
    import json
    try:
        with open(filename) as f_obj:
            numbers = json.load(f_obj)
        return numbers
    except Exception as e:
        return e


def instructions():
    print('\nПростой todo: \n1. Добавить задачу. \n2. Вывести список задач. \n3. Выход.')


command = 0
todo = list(reader("my_tasks.json"))

while command != 3:
    instructions()
    command = int(input('\nУкажите число: '))
    if command == 1:
        new = {}
        new['Task'] = input('СФормулируйте задачу: ')
        new['Category'] = input('Добавьте категорию к задаче: ')
        new['Date'] = input('Добавьте время к задаче: ')
        todo.append(new)
        writer('list_of_tasks.json', todo)

    if command == 2:
        print()
        for task in todo:
            print()
            for option in task:
                print(option, ':', task[option])

