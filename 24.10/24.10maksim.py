def py(*gyg):
    print(sum(gyg))
py(1, 2, 3, 4, 5,)



def yap(**nope):
    if 'privet' in nope.values():
        nope["privet"] = 'poka'
        print(nope)
    else:
        raise Exception('нет такого ключа')

yap(ажоф= "privet")


