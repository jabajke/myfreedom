


def hi(kak, ti):
    if not isinstance(kak, int) or not isinstance(ti, int):
        raise Exception('я принимаю только числа')
    elif kak + ti == 5:
        print(5 / 2)
    else:
        return (kak + ti)
print(hi('sasha chmo', 2))



