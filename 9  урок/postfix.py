def calc(lst):
    stack = []
    for i in lst:
        if i.isdigit():
            stack.append(int(i))
            continue

        l1 = stack.pop()
        l2 = stack.pop()
        l3 = {
            "+": lambda l2, l1: l2 + l1,
            "-": lambda l2, l1: l2 - l1,
            "/": lambda l2, l1: l2 / l1,
            "*": lambda l2, l1: l2 * l1
        }[i](l2, l1)
        stack.append(l3)
    return stack.pop()


lst = input("Введите набор цифр и символов: ").split()
print(calc(lst))
