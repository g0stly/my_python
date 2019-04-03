names = ['John', 'Paul', 'George', 'Ringo']

for i in names:
    if i != 'John' or i != 'Paul':
        names.remove(i)
print(names)
