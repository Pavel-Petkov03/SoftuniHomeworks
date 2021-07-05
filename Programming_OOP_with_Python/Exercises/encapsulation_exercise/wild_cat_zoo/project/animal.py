from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, gender, age):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    @abstractmethod
    def get_needs(self):
        pass
