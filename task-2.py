from abc import ABC, abstractmethod


class Cloths(ABC):
    def __init__(self, param):
        self.param = param

    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        if param < 50:
            self.__param = 50
        elif param > 240:
            self.__param = 240
        else:
            self.__param = param

    @property
    @abstractmethod
    def need_cloth(self):
        pass

    def __add__(self, other):
        return self.need_cloth + other.need_cloth


class Сoat(Cloths):

    @property
    def need_cloth(self):
        print(f"На пошив пальто необходимо {round(self.param / 6.5) + 0.5} ткани")
        return round(self.param / 6.5) + 0.5


class Suit(Cloths):

    @property
    def need_cloth(self):
        print(f"На пошив костюма необходимо {2 * self.param + 0.3} ткани")
        return 2 * self.param + 0.3


с_1 = Сoat(100)
s_1 = Suit(1000)

print(с_1 + s_1)
