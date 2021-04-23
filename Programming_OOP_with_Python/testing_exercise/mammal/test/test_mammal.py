from project.mammal import Mammal
import unittest


class MammalTests(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal('name', 'type', 'mql')

    def test__init__method(self):
        name = 'name'
        my_type = 'type'
        sound = 'mql'
        self.assertEqual(self.mammal.name, name)
        self.assertEqual(self.mammal.type, my_type)
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")
        self.assertEqual(self.mammal.sound, sound)

    def test_for_make_sound(self):
        expected = "name makes mql"
        self.assertEqual(self.mammal.make_sound(), expected)

    def test_for_get_kingdom(self):
        expected = 'animals'
        self.assertEqual(self.mammal.get_kingdom(), expected)

    def test_info(self):
        expected = f"name is of type type"
        self.assertEqual(self.mammal.info(), expected)
