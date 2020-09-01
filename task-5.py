my_list = [7, 5, 3, 3, 2]
print(f"Сейчас список выглядит так: {my_list}")

while True:
    rate = int(input("Введите натуральное число от 1 до 10 (чтобы выйти из программы введите 0): "))
    if 0 < rate <= 10:
        if rate < min(my_list):
            my_list.insert(len(my_list), rate)
        elif rate > max(my_list):
            my_list.insert(0, rate)
        else:
            new_list = my_list.copy()
            for j in my_list:
                if rate > j:
                    new_list.remove(j)
            my_list.insert(len(new_list), float(rate))
        print(my_list)
    elif rate == 0:
        break
    else:
        print("Вводимое целое число должно быть в промежутке от 1 до 10!")