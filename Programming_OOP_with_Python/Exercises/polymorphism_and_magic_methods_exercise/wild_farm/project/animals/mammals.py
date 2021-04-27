import math

from project.animals.animal import Animal
from abc import ABC, abstractmethod
from project.food import Fruit, Vegetable, Seed, Meat, Food


class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    @abstractmethod
    def feed(self, food):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        current_object_name = food.__class__.__name__
        if current_object_name == 'Vegetable' or current_object_name == 'Fruit':
            self.weight += food.quantity * 0.1
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {current_object_name}!"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        current_object_name = food.__class__.__name__
        if current_object_name == 'Meat':
            self.weight += food.quantity * 0.4
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {current_object_name}!"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        current_object_name = food.__class__.__name__
        if current_object_name == 'Meat':
            self.weight += food.quantity * 1.0
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {current_object_name}!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        current_object_name = food.__class__.__name__
        if current_object_name == 'Vegetable' or current_object_name == 'Meat':
            self.weight += food.quantity * 0.30
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {current_object_name}!"
