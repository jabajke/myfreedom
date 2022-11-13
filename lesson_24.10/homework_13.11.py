print('1)')
lst = [0, -20, 30, 23, 18, 120, 117]
lst_1 = list(filter(lambda x: x % 2 == 0, lst))
print(lst_1)

lst2 = [0, -20, 30, 23, 18, 120, 117]
lst3 = lst2[1:-2]
print(lst3)

lst4 = [0, -20, 30, 23, 18, 120, 117]
print(lst4[1], lst4[-1])


print('2)')
a = 'import time'
f = 'from time import *'
print(a)
print(f)


print('3)')
q ='интерпретируемый'
w = 'динамический'
e = 'объектно-ориентированный'
print(q)
print(w)
print(e)


print('4)')
a = 'Minsk'
b = 'Moscow'
c = 'Warsaw'
print('a) Minsk\n' 'b) Moscow\n' 'c) Warsaw\n' 'Столица Беларуси?')
ff = input()
while  ff == 'Minsk':
    print('Верно')
    if ff == b or c:
        print('Неверно, попробуйте ещё раз')
    else:
        print('Такого варианта не было')
print('НЕ ПОЛУЧИЛОСЬ У МЕНЯ 4 ЗАДАНИЕ')









