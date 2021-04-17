from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def make_sound(self):
        return 'bow'


class Chicken(Animal):
    def make_sound(self):
        return 'kudkudqk'


animals = [Cat(), Dog(), Chicken()]
for animal in animals:
    print(animal.make_sound())
