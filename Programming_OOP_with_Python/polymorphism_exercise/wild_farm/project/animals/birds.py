from food import Food
from animal import Animal
from abc import ABC, abstractmethod, abstractproperty


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food: object):
        pass

    def __repr__(self):
        return f"{1} [{self.__class__.__name__}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Owl(Bird):
    current_increase = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        current_object_name = food.__class__.__name__
        if current_object_name == 'Meat':
            self.weight += food.quantity * self.current_increase
        else:
            return f"{self.name} does not eat {food.__class__.__name__}!"


class Hen(Bird):
    current_increase = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.weight += food.quantity * self.current_increase

