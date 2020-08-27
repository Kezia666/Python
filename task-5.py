while True:
    income = int(input("Введите сумму выручки вашей фирмы: "))
    if income >= 0:
        while True:
            costs = int(input("Введите сумму издержек вашей фирмы: "))
            if costs >= 0:
                PL = income - costs
                if PL < 0:
                    print("К сожалению, ваша фирма работает в убыток.")
                elif PL == 0:
                    print("Ваша фирма работает в 0, что в целом не так плохо.")
                else:
                    print(f"Ура! У вашей фирмы есть прибыль - {PL}!")
                    print(f"Рентабельность вашей фирмы {(income - costs) / income * 100:.0f}%")
                    team = int(input("Введите количество сотрудников в вашей фирме: "))
                    print(f"Прибыль фирмы в расчете на одного сотрудника = {PL / team:.2f}")
                break
        break