class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
element = ""

while True:
    element = input("Введите целочисленный элемент списка (для завершения введите stop): ")
    if element.upper() == "STOP":
        break
    else:
        try:
            if element.isdigit() is True:
                my_list.append(int(element))
            else:
                raise OwnError("Введенное значение не является целочисленным!")
        except OwnError as err:
            print(err)

print(f"Итоговый список: {my_list}")
