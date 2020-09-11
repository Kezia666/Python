my_dict = {0: "Ноль", 1: "Один", 2: "Два", 3: "Три", 4: "Четыре", 5: "Пять", 6: "Шесть", 7: "Семь", 8: "Восемь",
           9: "Девять"}

with open("text_4.txt", "r", encoding="utf-8") as text_file:
    string_list = text_file.readlines()

with open("text_4_ru.txt", "w", encoding="utf-8") as text_file_ru:
    for i, string in enumerate(string_list):
        sign, number = string.split()[1], string.split()[2]
        text_file_ru.write(f"{my_dict[int(number)]} {sign} {number}")
        if i + 1 != len(string_list):
            text_file_ru.write("\n")
