def chislo(a):
    if not isinstance(a, int):
        raise Exception('Я принимаю только числа')
    elif a <= 34:
        print('мама')
    else:
        print('я')
chislo(271)

def summa(q, w):
    e = q + w
    if not isinstance(q, int) or not isinstance(w, int):
        raise Exception('Я принимаю только числа')
    elif e == 5:
        print(e / 2)
    else:
        print(e)

summa(4, 7)
