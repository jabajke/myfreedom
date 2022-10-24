#1
def project(a):
    if not isinstance(a, int):
        raise Exception('Я принимаю только числа')
    elif a <= 34:
        print('Иван')
    else:
        print('Александрa')
(project(33))
