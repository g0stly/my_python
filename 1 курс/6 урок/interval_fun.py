def f(x):
    return x**2 + 3


summary = 0
for y in range(10, 31, 2):
    summary += f(y)
print(summary)
