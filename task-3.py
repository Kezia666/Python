summa = 0
names = []

with open("text_3.txt", "r", encoding="utf-8") as text_file:
    string_list = text_file.readlines()

for string in string_list:
    name, salary = string.split()[0], string.split()[1]
    summa += float(salary)
    if float(salary) < 20000:
        names.append(name)

print(f"Фамилии сотрудников, чей оклад < 20000: {', '.join(names)}.")
print(f"Средний оклад по всей фирме = {round(summa / len(string_list), 2)}.")
