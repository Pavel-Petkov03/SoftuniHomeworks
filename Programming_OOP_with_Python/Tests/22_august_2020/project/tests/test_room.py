import unittest

from project.rooms.room import Room
from project.appliances.fridge import Fridge
from project.appliances.tv import TV


class RoomTest(unittest.TestCase):
    def setUp(self) -> None:
        self.r = Room('a', 12, 2)

    def test__init_(self):
        self.assertEqual(self.r.members_count, 2)
        self.assertEqual(self.r.budget, 12)
        self.assertEqual(self.r.family_name, 'a')
        self.assertEqual(self.r.children, [])
        self.assertTrue(hasattr(self.r, 'expenses'))

    def test_invalid_setter_expenses_in_expected_error(self):
        with self.assertRaises(ValueError) as ex:
            self.r.expenses = -1
            self.assertEqual(ex.exception, "Expenses cannot be negative")

    def test_calculate_expenses_expected_new_value_of_expenses_property(self):
        appliances = [TV(), Fridge()]
        self.r.calculate_expenses(appliances)
        self.assertEqual(81, self.r.expenses)






if __name__ == "__main__":
    unittest.main()
