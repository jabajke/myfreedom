'''def division(*args):
    print(sum(args))

division(1, 2, 3)'''


def fn(**kwargs):
    if'privet' in kwargs.values():
        kwargs['privet'] = 'poka'
        print(kwargs)
    else:
        raise Exception('такого нет в списке')





