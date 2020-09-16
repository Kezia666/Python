class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    pass

    def draw(self):
        print("Запуск отрисовки ручкой.")


class Pencil(Stationery):
    pass

    def draw(self):
        print("Запуск отрисовки карандашом.")


class Handle(Stationery):
    pass

    def draw(self):
        print("Запуск отрисовки маркером.")


stationery_1 = Stationery("Что-то канцелярское")
pen_1 = Pen("Ручка")
pencil_1 = Pencil("Карандаш")
handle_1 = Handle("Маркер")

stationery_1.draw()
pen_1.draw()
pencil_1.draw()
handle_1.draw()
