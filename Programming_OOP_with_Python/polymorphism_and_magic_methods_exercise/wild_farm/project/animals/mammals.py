from project.animals.animal import Animal
from abc import ABC, abstractmethod
from project.food import Fruit, Vegetable, Seed, Meat


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Mouse(Mammal):
    current_increase = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        current_object_name = food.__class__.__name__
        if current_object_name == 'Vegetable' or current_object_name == 'Fruit':
            self.weight += food.quantity * self.current_increase
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {current_object_name}!"


class Dog(Mammal):
    current_increase = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        current_object_name = food.__class__.__name__
        if current_object_name == 'Meat':
            self.weight += food.quantity * self.current_increase
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {current_object_name}!"


class Tiger(Mammal):
    current_increase = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        current_object_name = food.__class__.__name__
        if current_object_name == 'Meat':
            self.weight += food.quantity * self.current_increase
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {current_object_name}!"


class Cat(Mammal):
    current_increase = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        current_object_name = food.__class__.__name__
        if current_object_name == 'Vegetable' or current_object_name == 'Meat':
            self.weight += food.quantity * self.current_increase
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {current_object_name}!"
