class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", -1, 4)

import unittest


class CarManagerTests(unittest.TestCase):
    def setUp(self):
        self.my_car = Car("make", "model", 12, 12)

    def test___init___expected_valid__data(self):
        make = 'make'
        model = 'model'
        fuel_consumption = 12
        fuel_capacity = 12
        amount = 0
        self.assertEqual(self.my_car.make, make)
        self.assertEqual(self.my_car.model, model)
        self.assertEqual(self.my_car.fuel_consumption, fuel_consumption)
        self.assertEqual(self.my_car.fuel_capacity, fuel_capacity)
        self.assertEqual(self.my_car.fuel_amount, amount)

    def test___init__expected_fuel_consumption_exception(self):
        with self.assertRaises(Exception):
            self.new = Car('make', 'model', -1, 12)

    def test__init__expected_make_exception(self):
        with self.assertRaises(Exception):
            self.new = Car('', 'model', 12, 12)

    def test__init__expected_model_exception(self):
        with self.assertRaises(Exception):
            self.new = Car('make', '', 12, 12)

    def test___init__expected_fuel_capacity_exception(self):
        with self.assertRaises(Exception):
            self.new = Car('make', 'model', 12, -1)

    def test_make_getter(self):
        expected = 'make'
        actual = self.my_car.make
        self.assertEqual(actual, expected)

    def test_make_setter_with_null_element__expected_exception(self):
        with self.assertRaises(Exception):
            self.my_car.make = ''

    def test_make_setter_with_valid_data__expected_change_self__make(self):
        expected = 'new'
        actual = self.my_car.make = 'new'
        self.assertEqual(actual, expected)

    def test_model_getter(self):
        expected = 'model'
        self.assertEqual(self.my_car.model, expected)

    def test_model_setter_with_null_element__expected_exception(self):
        with self.assertRaises(Exception):
            self.my_car.model = ''

    def test_model_setter_with_valid_data__expected_new_value_of___model(self):
        expected = 'new'
        actual = self.my_car.model = 'new'
        self.assertEqual(actual, expected)

    def test_fuel_consumption_getter(self):
        expected = 12
        actual = self.my_car.fuel_consumption
        self.assertEqual(actual, expected)

    def test_fuel_consumption_setter_with_null_element__expected_exception(self):
        with self.assertRaises(Exception):
            self.my_car.fuel_consumption = -1

    def test_fuel_consumption_setter_with_valid_data__expected_new_value_of___fuel_consumption(self):
        expected = 3
        actual = self.my_car.fuel_consumption = 3
        self.assertEqual(actual, expected)

    def test_fuel_capacity_getter(self):
        expected = 12
        self.assertEqual(self.my_car.fuel_capacity, expected)

    def test_fuel_capacity_setter_with_null_element__expected_exception(self):
        with self.assertRaises(Exception):
            self.my_car.fuel_capacity = -1

    def test_fuel_capacity_setter_with_valid_data__expected_new_value_of___fuel_capacity(self):
        expected = 3
        actual = self.my_car.fuel_capacity = 3
        self.assertEqual(actual, expected)

    def test_fuel_amount_getter(self):
        expected = 0
        actual = self.my_car.fuel_amount
        self.assertEqual(actual, expected)

    def test_fuel_amount_setter_with_null_element__expected_exception(self):
        with self.assertRaises(Exception):
            self.my_car.fuel_amount = -1

    def test_fuel_amount_setter_with_valid_data__expected_new_value_of__fuel_amount(self):
        expected = 3
        actual = self.my_car.fuel_amount = 3
        self.assertEqual(actual, expected)

    def test_refuel_function__with_negative_fuel__expected_exception(self):
        with self.assertRaises(Exception):
            self.my_car.refuel(-1)

    def test_refuel_function_with_new_amount_which_is_less_or_equal_to_fuel_capacity__expected_increase_of_fuel_amount(
            self):
        expected_new_amount = 3
        self.my_car.refuel(3)
        self.assertEqual(expected_new_amount, self.my_car.fuel_amount)

    def test_refuel_function_with_new_amount_which_is_greater_than_fuel_capacity__expected_fuel_amount_equal_fuel_capacity(
            self):
        expected_new_amount = 12
        self.my_car.refuel(13)
        self.assertEqual(expected_new_amount, self.my_car.fuel_amount)

    def test_drive_needed_greater_than_amount__expected_exception(self):
        with self.assertRaises(Exception):
            self.my_car.drive(120)

    def test_drive_decrease_of_fuel_amount(self):
        expected = 0
        self.my_car.fuel_amount = 12
        self.my_car.drive(100)
        self.assertEqual(self.my_car.fuel_amount, expected)


if __name__ == "__main__":
    unittest.main()
