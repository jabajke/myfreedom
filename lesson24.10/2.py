def nn(**kwargs):
    if 'privet' in kwargs.values():
        kwargs['privet'] = 'poka'
        print(kwargs)
    else:
        raise Exception('Нет этого')


nn(asd='privet', poka='asd')
