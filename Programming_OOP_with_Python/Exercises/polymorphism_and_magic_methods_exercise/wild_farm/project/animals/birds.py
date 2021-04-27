from project.food import Vegetable, Seed, Fruit, Meat
from project.animals.animal import Animal
from abc import ABC, abstractmethod


class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

    @abstractmethod
    def feed(self, food):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Owl(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        current_object_name = food.__class__.__name__
        if current_object_name == 'Meat':
            self.weight += food.quantity * 0.25
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {current_object_name}!"


class Hen(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity
