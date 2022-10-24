def neogran(*args):
    print(sum(args))
neogran(1, 2, 3, 4, 5)


def mnogo(**kawargs):
    if 'privet' in kawargs.values():
        kawargs['privet'] = 'poka'
        print(kawargs)
    else:
        raise Exception('нету')
mnogo(asd='ff', qwe='privet', privet= 'adad')


