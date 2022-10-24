def z1(*args):
    print(sum(args))


z1(1, 3, 6, 5)


def z2(**kwargs):
    if 'privet' in kwargs.values():


z2(privet='privet')

def z3(*args, **kwargs):
    try:
        print(sum(*args.multiply()))
