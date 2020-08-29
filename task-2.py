while True:
    sec = int(input("Введите время в секундах (число от 0 до 86399): "))
    if 0 <= sec <= 86399:
        hh = sec // 3600
        mm = sec % 3600 // 60
        ss = sec % 3600 % 60
        print(f"Время в формате (чч:мм:сс): {hh:02}:{mm:02}:{ss:02}")
        break