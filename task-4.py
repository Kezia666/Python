while True:
    n = int(input("Введите целое положительное число: "))
    if n > 0:
        digit = 0

        while True:
            if n % 10 > digit:
                digit = n % 10
            if digit == 9 or n < 10:
                break
            n = n // 10

        print(f"Самая большая цифра в вашем числе - {digit}")
        break