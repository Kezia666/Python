class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 100, "bonus": 10}


class Position(Worker):
    def get_full_name(self):
        print(f"{self.surname} {self.name}")

    def get_total_income(self):
        print(f"{self._income['wage'] + self._income['bonus']}")


position_1 = Position("Alena", "Morozova", "programmer")
print(position_1.name)
print(position_1.position)
position_1.get_full_name()
position_1.get_total_income()
