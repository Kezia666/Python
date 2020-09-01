# Объявление переменных
items = []
item = []
analysis_item = []
desc = {}
analysis = {}
item_count = 0

# Список характеристик товара, который можно расширить при необходимости
features = {"название": "Название", "цена": "Цена", "количество": "Количество", "ед": "Единицы измерения"}

print("Добро пожаловать на сайт!")

while True:
    menu = int(input("Чтобы ввести информацию о товаре - 1; чтобы просмотреть аналитику - 2; чтобы выйти из программы - 3: "))
    if menu == 1:
        item_count += 1
        print("Введите значения характеристик товара:")
        for key, value in features.items():
            feature = input(f"{value}: ")
            if feature.isdigit():
                desc[key] = int(feature)
            else:
                desc[key] = feature
        item.append(item_count)
        item.append(desc.copy())
        items.append(tuple(item))
        item.clear()
        print(items)
    elif menu == 2:
        for key, value in features.items():
            for i in items:
                analysis_item.append(i[1][key])
            analysis[key] = list(set(analysis_item.copy()))
            analysis_item.clear()
        print(analysis)
    else:
        print("До свидания!")
        break