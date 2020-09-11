import random

my_list = []
summa = 0

while len(my_list) != 10:
    my_list.append(str(random.randint(1, 10)))

with open("text_5.txt", "w", encoding="utf-8") as text_file:
    text_file.write(' '.join(my_list))

with open("text_5.txt", "r", encoding="utf-8") as text_file:
    string = text_file.read()

for n in string.split():
    summa += int(n)

print(string)
print(summa)
