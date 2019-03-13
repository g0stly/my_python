from math import sqrt

data = [2, 4, 9, 16, 25]


newList1 = []
for i in range(len(data)):
    newList1.append(sqrt(data[i]))
print('С помощью цикла "for":', newList1)

newList2 = list(map(sqrt, data))
print('С помощью функции "map":', newList2)

newList3 = [sqrt(data[i]) for i in range(len(data))]
print('С помощью генератора списка:', newList3)
