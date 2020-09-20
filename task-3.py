class Cell:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return self.param + other.param

    def __sub__(self, other):
        return self.param - other.param if self.param > other.param else other.param - self.param

    def __mul__(self, other):
        return self.param * other.param

    def __floordiv__(self, other):
        return self.param // other.param if self.param > other.param else other.param // self.param

    def make_order(self, in_row):
        count = 0
        row = []
        for i in range(self.param):
            row.append('*')
            count += 1
            if count == in_row:
                row.append('\n')
                count = 0
        string = ''.join(row)
        return string


cell_1 = Cell(5)
cell_2 = Cell(10)
print(cell_1.param)
print(cell_2.param)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(4))
