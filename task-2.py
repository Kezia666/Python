class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    m = float(input("Введите делимое: "))
    n = float(input("Введите делитель: "))
    if n == 0:
        raise OwnError("Деление на 0 невозможно!")
    else:
        print(round(m / n, 2))
except OwnError as err:
    print(err)
