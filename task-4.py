class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала!")

    def stop(self):
        print("Машина остановилась!")

    def turn(self, direction):
        print(f"Машина повернула {direction}!")

    def show_speed(self):
        print(f"Текущая скорость автомобиля = {self.speed}!")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости!")


class PoliceCar(Car):
    pass


Car_1 = TownCar(50, "yellow", "Toyota", False)
Car_2 = SportCar(50, "red", "Honda", False)
Car_3 = WorkCar(50, "green", "Volvo", False)
Car_4 = PoliceCar(50, "blue", "Skoda", True)

Car_1.go()
Car_2.stop()

Car_1.show_speed()
Car_2.show_speed()
Car_3.show_speed()
Car_4.show_speed()

Car_1.turn("направо")
