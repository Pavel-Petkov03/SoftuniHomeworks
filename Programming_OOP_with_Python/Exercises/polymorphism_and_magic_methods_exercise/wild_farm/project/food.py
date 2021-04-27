from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def __init__(self, q):
        self.quantity = q


class Fruit(Food):
    def __init__(self, q):
        super().__init__(q)


class Vegetable(Food):
    def __init__(self, q):
        super().__init__(q)


class Meat(Food):
    def __init__(self, q):
        super().__init__(q)


class Seed(Food):
    def __init__(self, q):
        super().__init__(q)
