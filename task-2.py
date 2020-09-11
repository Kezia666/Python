string = None

with open("text_file.txt", "a+", encoding="utf-8") as text_file:
    while True:
        string = input("Введите строку, которую вы хотите добавить в файл. Пустая строка - окончание ввода: ")
        if string != "":
            if text_file.tell() != 0:
                text_file.write("\n")
            text_file.write(string)
        else:
            break
    text_file.seek(0)
    string_list = text_file.readlines()

print(f"Содержание файла: {string_list}\nКоличество строк: {len(string_list)}")
for i, string in enumerate(string_list):
    print(f"Количество слов в {i + 1} строке = {len(string.split())}")
