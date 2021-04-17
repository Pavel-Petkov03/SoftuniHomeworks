from abc import ABC, abstractmethod


class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shapes):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class AreaCalculator:
    def __init__(self, shapes: list[Shapes]):
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()
        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
