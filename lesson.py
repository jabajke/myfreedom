def num(a):
    if not isinstance(a, int):
        raise Exception('Я примнимаю только числа')
    elif a <= 34:
        print('nastya')
    else:
        print('mum')


num(3)


def num2(a, b):
    s = a + b
    if not isinstance(a or b, int):
        raise Exception('Я примнимаю только числа')
    elif s == 5:
        return s / 2
    else:
        print(s)
num2(1, 3)
