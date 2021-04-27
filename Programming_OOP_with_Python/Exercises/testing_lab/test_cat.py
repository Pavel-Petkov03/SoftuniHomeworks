class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    name = 'Pavkata'

    def setUp(self):
        self.cat = Cat(self.name)

    def test_check_eating_function_expected_cat_increase_size(self):
        """
        Cat's size is increased after eating
        """
        start = self.cat.size
        self.cat.eat()
        self.assertEqual(start + 1, self.cat.size)

    def test_check_cat_fed_after_eating_expected_bool(self):
        """
        Cat is fed after eating
        """
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_eat_and_already_fed_expected_error(self):
        """
        Cat cannot eat if already fed, raises an error
        """
        self.cat.fed = True
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_fall_asleep_and_not_fed__expected_raise_error(self):
        """
        Cat cannot fall asleep if not fed, raises an error
        """
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_not_sleepy_after_sleeping(self):
        """
        Cat is not sleepy after sleeping
        """
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()
