def my_func(p1, p2):
    try:
        print(p1 / p2)
    except ZeroDivisionError:
        print("Деление на 0 невозможно!")

x1 = float(input("Введите делимое: "))
x2 = float(input("Введите делитель: "))

my_func(x1, x2)
