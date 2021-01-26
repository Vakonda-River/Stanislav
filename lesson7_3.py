# -*- coding: utf8 -*-
class Cell:
    __count_cell: int

    def __init__(self, count: int):
        self.__count_cell = count

    def item_setting(self, other):
        assert isinstance(other, self.__class__)

    def __add__(self, other: 'Cell'):
        self.item_setting(other)
        value = self.count + other.count
        return f"Сложение, {Cell(value)}"

    def __sub__(self, other: 'Cell'):
        self.item_setting(other)
        value = self.count - other.count
        return f"Вычитание, {Cell(value)}"

    def __mul__(self, other: 'Cell'):
        self.item_setting(other)
        value = self.count * other.count
        return f"Умножение, {Cell(value)}"

    def __truediv__(self, other: 'Cell'):
        self.item_setting(other)
        value = round(self.count / self.count)
        return f"Деление, {Cell(value)}"

    def __str__(self):
        return f"pезультат = {self.__count_cell}"

    @ property
    def count(self):
        return self.__count_cell

    @ staticmethod
    def construction (cell_object: 'Cell', count_in_row: int):
        items = '*' * cell_object.count
        parts = [items[q:q + count_in_row] for q in range(0, len(items), count_in_row)]
        return '\n'.join(parts)

cell_1= Cell(5)
cell_2 = Cell(4)
row_cell = Cell(18)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print(Cell.construction(row_cell, 5))
