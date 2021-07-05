import unittest

from project.animal import Animal
from project.cat import Cat
from project.dog import Dog


class Tests(unittest.TestCase):
    def test_animal(self):
        a = Animal()
        self.assertEqual(a.eat(), "eating...")

    def test_dog(self):
        a = Dog()
        self.assertEqual(a.bark(), "barking...")
        self.assertEqual(a.__class__.__bases__[0].__name__, "Animal")

    def test_cat(self):
        a = Cat()
        self.assertEqual(a.meow(), "meowing...")
        self.assertEqual(a.__class__.__bases__[0].__name__, "Animal")


if __name__ == "__main__":
    unittest.main()