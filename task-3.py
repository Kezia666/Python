while True:
    n = int(input("Введите число n: "))
    if n > 0:
        nn = int(f"{n}{n}")
        nnn = int(f"{n}{n}{n}")
        print(n + nn + nnn)
        break