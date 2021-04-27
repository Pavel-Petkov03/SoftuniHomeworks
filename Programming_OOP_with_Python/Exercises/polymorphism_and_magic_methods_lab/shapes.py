from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, h, w):
        self.__height = h
        self.__width = w

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)



rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

