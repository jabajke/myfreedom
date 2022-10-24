def firfun (*args):
    print(sum(args))

firfun(4, 2, 5)

def secfun (**kwargs):
    if 'privet' in kwargs.values():
        kwargs['privet'] = 'poka'
        print(kwargs)
    else: raise Exception('Нет такого ключа')

secfun(a='privet')
