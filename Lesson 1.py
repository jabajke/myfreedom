def tt(a, b):
    if not isinstance(a, int):
        raise Exception('Я принимаю только числа')
    elif not isinstance(b, int):
        raise Exception('Я принимаю только числа')
    elif a + b == 5:
        print(5/2)
    else:
        print(a+b)

tt(5, '3')

