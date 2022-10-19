def division(a):
    if not isinstance(a, int):
        raise Exception('Я принимаю только числа')
    if a <= 34:
        print('Mama')
    else:
        print('my_name')
division(34)

def division_2(a, b):
    if not isinstance(a,int) or not isinstance(b, int):
        raise ('Я принимаю только числа')
    if a * b >= 5:
        print(a/2 * b/2)
    else:
        print(a*b)
division_2(4, 5)


def division_3(a):
    if not isinstance(a, str):
        raise Exception('haha')
    elif len(a) < 5:
        print(a)
    else:
        print('haha')
