# -*- coding: utf8 -*-
class Matrix:
    value: list 

    def __init__(self, value: list):
        self.value = value

    def __str__(self):
        return "\n".join(str(row) for row in self.value)

    def __add__(self, new: 'Matrix'):

        rows_count = len(self.value)
        items_count = len(self.value[0])

        new_v = [
            [
                self.value[row][idx] + new.value[row][idx] for idx in range(items_count)
            ]
            for row in range(rows_count)
        ]
        return Matrix(new_v)

a = Matrix([
    [10, 20, 30],
    [11, 12, 13],
])

b = Matrix([
    [40, 50, 60],
    [21, 22, 23],
])

c = a + b
print("Результат сложения матриц:")
print(c)
