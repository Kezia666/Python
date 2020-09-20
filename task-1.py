import random


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        for_print = []
        for i in self.data:
            string = ' '.join(map(lambda x: f"{str(x):2}", i))
            for_print.append(string)
        return '\n'.join(for_print)

    def __add__(self, other):
        new_matrix = []
        new_row = []
        for i, val_1 in enumerate(self.data):
            for j, val_2 in enumerate(val_1):
                new_row.append(self.data[i][j] + other.data[i][j])
            new_matrix.append(new_row.copy())
            new_row.clear()
        return Matrix(new_matrix)


def create_data():
    data = []
    row = []
    while len(data) < 10:
        while len(row) < 10:
            row.append(random.randint(0, 9))
        data.append(row.copy())
        row.clear()
    return data


mt1 = Matrix(create_data())
mt2 = Matrix(create_data())

# print(mt1.data)
# print(mt2.data)
print('* ' * 50)
print(mt1)
print('* ' * 50)
print(mt2)
print('* ' * 50)
print(mt1 + mt2)
print('* ' * 50)