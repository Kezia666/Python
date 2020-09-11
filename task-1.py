string = None

with open("text_file.txt", "w", encoding="utf-8") as text_file:
    while True:
        string = input("Введите строку, которую вы хотите добавить в файл. Пустая строка - окончание ввода: ")
        if string != "":
            if text_file.tell() != 0:
                text_file.write("\n")
            text_file.write(string)
        else:
            break
