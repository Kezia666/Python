def my_func(x, y):
    res = 1
    while y < 0:
        res *= x
        y += 1
    return (1 / res)


x = float(input("Введите x (действительное положительное число): "))
y = float(input("Введите y (отрицательное целое число): "))
print(my_func(x, y))