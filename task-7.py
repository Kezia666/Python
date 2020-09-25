class Complex:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def __str__(self):
        return f"Комплексное число: {self.x1}{'' if self.x2 < 0 else '+'}{self.x2}i"

    def __add__(self, other):
        return f"{self.x1 + other.x1}{'' if self.x2 + other.x2 < 0 else '+'}{self.x2 + other.x2}i"

    def __mul__(self, other):
        n = (self.x1 * other.x1) + (self.x2 * other.x2 * -1)
        m = self.x1 * other.x2 + self.x2 * other.x1
        return f"{n}{'' if m < 0 else '+'}{m}i"


c1 = Complex(1, -1)
c2 = Complex(3, 6)
print(c1)
print(c2)
print(f"Результат сложения комплексных чисел: {c1 + c2}")
print(f"Результат произведения комплексных чисел: {c1 * c2}")
