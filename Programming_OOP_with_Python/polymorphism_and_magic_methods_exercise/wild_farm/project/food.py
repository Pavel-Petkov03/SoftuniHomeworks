from abc import ABC, abstractmethod


class Food(ABC):
    def __init__(self, q):
        self.quantity = q


class Fruit(Food):
    pass


class Vegetable(Food):
    pass


class Meat(Food):
    pass


class Seed(Food):
    pass
