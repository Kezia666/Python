class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self, thickness=5, sm1=25):
        return f"Масса асфальта, необходимого для покрытия всего дорожного полотна = {round(self._length * self._width * thickness * sm1 / 1000)} тонн."


road_1 = Road(5000, 20)
print(road_1.massa())
