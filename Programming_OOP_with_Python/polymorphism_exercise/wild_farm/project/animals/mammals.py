from Programming_OOP_with_Python.polymorphism_exercise.wild_farm.project.animals.birds import Owl
from Programming_OOP_with_Python.polymorphism_exercise.wild_farm.project.animals.food import Meat, Vegetable
from animal import Animal
from abc import ABC, abstractmethod


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.name} [{self.__class__.__name__}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass


class Mouse(Mammal):
    current_increase = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        current_object_name = food.__name__
        if current_object_name == 'Vegetable' or current_object_name == 'Fruit':
            self.weight += food.quantity * self.current_increase
            self.food_eaten += food.quantity
        else:
            return f"{self.name} does not eat {food.__name__}!"


class Dog(Mammal):
    current_increase = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        current_object_name = food.__name__
        if current_object_name == 'Meat':
            self.weight += food.quantity * self.current_increase
            self.food_eaten += food.quantity
        else:
            return f"{self.__name__} does not eat {food.__name__}!"


class Tiger(Mammal):
    current_increase = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        current_object_name = food.__name__
        if current_object_name == 'Meat':
            self.weight += food.quantity * self.current_increase
            self.food_eaten += food.quantity
        else:
            return f"{self.__name__} does not eat {food.__name__}!"


class Cat(Mammal):
    current_increase = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        current_object_name = food.__name__
        if current_object_name == 'Vegetable' or current_object_name == 'Meat':
            self.weight += food.quantity * self.current_increase
            self.food_eaten += food.quantity
        else:
            return f"{self.__name__} does not eat {food.__name__}!"


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
