import re

my_dict = {}

with open("text_6.txt", "r", encoding="utf-8") as text_file:
    string_list = text_file.readlines()

for string in string_list:
    hours = 0
    subject = string[0:string.index(":")]
    for i in string.split("("):
        try:
            hours += int(re.sub(r"\D", "", i))
        except:
            continue
    my_dict[subject] = hours

print(my_dict)
