# 1. В функцию поступает неограниченное число неименованных аргументов,
# 	Ваша задача - сложить все эти аргументы и вывести

# 2. В функцию поступают неограниченное количество именнованных аргументов,
# 	Ваша задача - проверить, есть ли в итоговом словаре значение 'privet', если есть,
# 	то добавить к этому словарю ключ 'privet' со значением 'poka', если нет,
# 	то вывести ошибку через raise
# 	для того, чтобы достать все ключи словаря, нужно к нему обратиться
# 	и вызвать метод keys() или values() если нужны значения.


def fn(**kwargs):
    if 'privet' in kwargs.values():
        kwargs['privet'] = 'poka'
        print(kwargs)
    else:
        raise Exception('Нет такого значения')


fn(aosdasd='privet', asijdh='akjksdb', asd=100)
