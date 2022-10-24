lst = []
a = int(input("Введите количесло чисел: "))
for i in range(a):
    b = int(input("Введите числа: "))
    lst.append(b)
    if b > 0:
        print("положительное")
        lst.append(b)
        print(lst)
