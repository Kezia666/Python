while True:
    sec = int(input("Введите время в секундах (число от 0 до 86399): "))
    if 0 <= sec <= 86399:

        # Condition for hh
        if sec // 3600 < 10:
            hh = f"0{str(sec // 3600)}"
        else:
            hh = f"{str(sec // 3600)}"

        # Condition for mm
        if sec % 3600 // 60 < 10:
            mm = f"0{str(sec % 3600 // 60)}"
        else:
            mm = f"{str(sec % 3600 // 60)}"

        # Condition for ss
        if sec % 3600 % 60 < 10:
            ss = f"0{str(sec % 3600 % 60)}"
        else:
            ss = f"{str(sec % 3600 % 60)}"

        # Output
        print(f"{hh}:{mm}:{ss}")
        break