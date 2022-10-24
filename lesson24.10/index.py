def numbers(*args):
    print(sum(args))
numbers(1, 3, 5)

def fn(**kwargs):
    if 'privet' in kwargs.values():
        kwargs['privet']= 'poka'
    else:
        raise  Exception('404')
fn()


