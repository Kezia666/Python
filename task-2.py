my_list = []
new_list = []

while True:
    item = input("Введите значение элемента списка. Если вы ввели достаточно значений - введите 'end': ")
    if item != "end":
        my_list.append(item)
    else:
        break

print(my_list)

for i, j in enumerate(my_list):
    if (i + 2) % 2 == 0:
        my_list.pop(i)
        my_list.insert(i+1, j)

print(my_list)