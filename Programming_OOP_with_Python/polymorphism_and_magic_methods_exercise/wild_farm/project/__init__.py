# first zero test
import unittest
from project.animals.birds import Owl, Hen
from project.animals.mammals import Mouse, Dog, Cat, Tiger
from project.food import Vegetable, Fruit, Meat, Seed

class WildFarmTests(unittest.TestCase):
    def test_first_zero(self):
        owl = Owl("Pip", 10, 10)
        self.assertEqual(str(owl), "Owl [Pip, 10, 10, 0]")
        meat = Meat(4)
        self.assertEqual(owl.make_sound(), "Hoot Hoot")
        owl.feed(meat)
        veg = Vegetable(1)
        owl.feed(veg)
        self.assertEqual(owl.feed(veg), "Owl does not eat Vegetable!")
        self.assertEqual(str(owl), "Owl [Pip, 10, 11.0, 4]")

if __name__ == "__main__":
    unittest.main()


