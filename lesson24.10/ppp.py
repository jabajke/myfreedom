def division(*args):
    print(sum(args))


division(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


def division_2(**kwargs):
    if 'privet' in kwargs.values():
        kwargs['privet'] = 'poka'
    else:
        raise Exception('hahahaha')
    print(kwargs)


division_2(poka='privet')


def division_3(*args, **kwargs):
    if 'multiply' in kwargs.keys():
        try:
            s = sum(args) + kwargs['multiply']
        except Exception:
            print('ti ne pododish')



division_3(1, 2, 3, 4, 5, 6, 7, 8, 9, multiply='aaa')
