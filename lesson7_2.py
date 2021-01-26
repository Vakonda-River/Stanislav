# -*- coding: utf8 -*-

class Clothes():
    type: str

    def __init__(self, type: str):
        self.type = type

class Coat(Clothes):
    _size: float

    def __init__(self, type: str, size: float):
        super().__init__(type)
        self._size = size

    @ property
    def calculate(self) -> float:
        return f"{self.type}{self._size / 6.5 + 0.5}"

class Suit(Clothes):
    _height: float

    def __init__(self, type: str, height: float):
        super().__init__(type)
        self._height = height

    @ property
    def calculate(self) -> float:
        return f"{self.type}{2 * self._height + 0.3}"

coat = Coat('Пальто = ', 3)
print(coat.calculate)

suit = Suit('Костюм = ', 1.8)
print(suit.calculate)
