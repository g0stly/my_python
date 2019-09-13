tempList = {}

with open("temper.stat.txt", 'r') as file:
    contents = file.read()

for temp in contents.split():
    tempList.append(float(temp))


print('Максимальная температура: ', max(tempList),
      '\nМинимальная температура: ', min(tempList),
      '\nСредняя температура: ', sum(tempList)/len(tempList),
      '\nКоличество уникальных температур: ', len(set(tempList))
      )
