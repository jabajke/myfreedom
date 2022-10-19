def division(a):
    if not isinstance(a, int):
        print(ValueError('no'))
    elif a<=34:
        print('Timur')
    elif a>34:
        print('Mama')
division('apapapa')

def division_2(x,y):
    if not isinstance(x, int):
        print(ValueError('no'))
    elif not isinstance(y, int):
        print(ValueError('no'))
    elif x+y==5:
        print((x+y)/2)
    else:
        print(x+y)
division_2('asas',2)

def division_3(a):
    if not isinstance(a,str):
        print(ValueError('no'))
    elif len(a)<5:
        print(a)
    elif len(a)>=5:
        print('Я устал босс')
division_3('mamaaa')