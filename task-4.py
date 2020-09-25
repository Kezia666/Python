import json
from prettytable import PrettyTable

wh_list = []


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self, wh_name, path=""):
        self.wh_name = wh_name
        self.path = path
        wh_list.append({len(wh_list) + 1: wh_name})
        try:
            with open(f"{path}{wh_name}.json", "x") as new:
                json.dump([], new)
        except FileExistsError:
            pass
            # print(f"New warehouse file '{wh_name}.json' was not created, because it already exists.")

    def print_wh(self):
        print(f"Warehouse name: {self.wh_name}")
        headers = ["Item Type", "Title", "Model", "Printer Type", "Colored Printer"]
        data = []
        t = PrettyTable(headers)
        for list_item in self.show_wh():
            for key, value in list_item.items():
                if key == "printer_features":
                    for printer_feature in value.values():
                        data.append(f"{printer_feature}")
                else:
                    data.append(f"{value}")
            if len(list_item) == 3:
                data.append("None")
                data.append("None")
            t.add_row(data)
            data.clear()
        print(t)

    def show_wh(self):
        with open(f"{self.path}{self.wh_name}.json", "r") as wh:
            return json.load(wh)

    def add_to_wh(self, item="", from_file=False, file_name="add", path=""):
        if not from_file:
            try:
                new_data = [{"item_type": item.item_type, "title": item.title, "model": item.model,
                             "printer_features": {"printer_type": item.printer_type, "colored": item.colored}}]
            except AttributeError:
                new_data = [{"item_type": item.item_type, "title": item.title, "model": item.model}]
        else:
            with open(f"{path}{file_name}.json", "r") as add:
                new_data = json.load(add)
        all_data = self.show_wh()
        all_data.extend(new_data)
        with open(f"{self.path}{self.wh_name}.json", "w") as wh_new:
            json.dump(all_data, wh_new)
        print(f"{self.wh_name} warehouse current state:\n{self.print_wh()}")

    def delete_from_wh(self, item):
        all_data = self.show_wh()
        for value in all_data:
            if value["item_type"] == item.item_type and value["title"] == item.title and value["model"] == item.model:
                all_data.remove(value)
        with open(f"{self.path}{self.wh_name}.json", "w") as wh:
            json.dump(all_data, wh)
        print(f"{self.wh_name} warehouse current state:\n{self.print_wh()}")

    def move_to_wh(self, item, to_wh):
        self.delete_from_wh(item)
        to_wh.add_to_wh(item)

    def show_analytics(self):
        all_data = self.show_wh()
        print('*' * 43)
        print(f"Total items on warehouse {self.wh_name}: {len(all_data)}")
        print('*' * 43)
        p, s, x = 0, 0, 0
        for value in all_data:
            if value['item_type'].lower() == 'printer':
                p += 1
            elif value['item_type'].lower() == 'scanner':
                s += 1
            else:
                x += 1
        print(f"* Printers: {p}")
        print(f"* Scanners: {s}")
        print(f"* Xeroxes: {x}")
        print('*' * 43, '\n')


class TechItems:
    def __init__(self, item_type, title, model):
        self.item_type = item_type
        self.title = title
        self.model = model


class Printer(TechItems):
    def __init__(self, item_type, title, model, printer_type, colored):
        super().__init__(item_type, title, model)
        self.printer_type = printer_type
        self.colored = colored


class Scanner(TechItems):
    pass


class Xerox(TechItems):
    pass


wh1 = Warehouse("WH1")
wh2 = Warehouse("WH2")
# sc = Scanner("Scanner", "Test", "Test")
# pr = Printer("Printer", "Title", "Model", "struinyi", True)
# xs = Xerox("Xerox", "Test", "Test")
# wh1 = Warehouse("WH1")
# wh2 = Warehouse("WH2", "")
# wh1.add_to_wh(pr)
# wh1.delete_from_wh(pr)
# wh1.show_analytics()
# wh1.show_analytics()
# main.move_to_wh(sc, wh1)
# main.print_wh()

menu = PrettyTable(["Menu", "Enter Number"])
menu.add_row(["To see the list of existing warehouses", 1])
menu.add_row(["To see the list of items in warehouses", 2])
menu.add_row(["To add new printer (to WH1)", 3])
menu.add_row(["To add new scanner (to WH1)", 4])
menu.add_row(["To add new xerox (to WH1)", 5])
menu.add_row(["To move item from WH1 to WH2", 6])
menu.add_row(["To delete item from WH1", 7])
menu.add_row(["To delete item from WH2", 8])
menu.add_row(["To see analytics", 9])
menu.add_row(["To exit the program", 10])

print('*' * 43)
print("* Welcome to warehouse management system! *")
print('*' * 43)
while True:
    print(f"\n{menu}\n")
    menu_num = int(input("Enter number: "))
    if menu_num == 1:
        for list_item in wh_list:
            for key, value in list_item.items():
                print(f"{key} - {value}")
    elif menu_num == 2:
        wh1.print_wh()
        wh2.print_wh()
    elif menu_num == 3:
        title = input("Enter printer brand name: ")
        model = input("Enter printer model: ")
        while True:
            try:
                printer_type = input("Is it laser (L) or ink-jet (I)? ")
                if printer_type.upper() not in ["L", "I"]:
                    raise OwnError("Incorrect value! Print 1 (laser) or 2 (ink-jet)!")
                else:
                    printer_type = "laser" if printer_type.upper() == "L" else "ink-jet"
                    break
            except OwnError as err:
                print(err)
        while True:
            try:
                colored = input("Is it colored (T/F)? ")
                if colored.upper() not in ["T", "F"]:
                    raise OwnError("Incorrect value! Print T (true) or F (false)!")
                else:
                    colored = True if colored.upper() == 'T' else False
                    break
            except OwnError as err:
                print(err)
        pr = Printer("Printer", title, model, printer_type, colored)
        wh1.add_to_wh(pr)
    elif menu_num == 4:
        title = input("Enter scanner brand name: ")
        model = input("Enter scanner model: ")
        sc = Scanner("Scanner", title, model)
        wh1.add_to_wh(sc)
    elif menu_num == 5:
        title = input("Enter xerox brand name: ")
        model = input("Enter xerox model: ")
        xs = Xerox("Xerox", title, model)
        wh1.add_to_wh(xs)
    elif menu_num == 6:
        wh1.move_to_wh(pr, wh2)         # здесь нужно будет реализовать через ID устройства на складе
    elif menu_num == 7:
        wh1.delete_from_wh(pr)         # здесь нужно будет реализовать через ID устройства на складе
    elif menu_num == 8:
        wh2.delete_from_wh(pr)         # здесь нужно будет реализовать через ID устройства на складе
    elif menu_num == 9:
        wh1.show_analytics()
        wh2.show_analytics()
    elif menu_num == 10:
        break
print("Good bye!")
