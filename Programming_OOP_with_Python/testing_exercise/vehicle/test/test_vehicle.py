from unittest import TestCase

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(12, 100)

    def test__init__(self):
        fuel = 12
        horsepower = 100
        capacity = 12
        fuel_consumption = 1.25
        self.assertEqual(fuel, self.vehicle.fuel)
        self.assertEqual(horsepower, self.vehicle.horse_power)
        self.assertEqual(capacity, self.vehicle.capacity)
        self.assertEqual(fuel_consumption, self.vehicle.fuel_consumption)
        self.assertEqual(fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_fuel_less_than_needed__expected_exception(self):
        with self.assertRaises(Exception) as exp:
            self.vehicle.drive(100)
        self.assertEqual(str(exp.exception), "Not enough fuel")

    def test_drive_fuel_more_than_needed__expected_fuel_to_decrease_from_needed(self):
        expected_new_fuel = 7
        self.vehicle.drive(4)
        self.assertEqual(self.vehicle.fuel, expected_new_fuel)

    def test_refuel_bigger_than_capacity__expected_exception(self):
        with self.assertRaises(Exception) as exp:
            self.vehicle.refuel(1)
        self.assertEqual(str(exp.exception), "Too much fuel")

    def test_refuel_less_or_equal_than_capacity_expected_increase(self):
        self.vehicle.capacity = 100
        self.vehicle.refuel(68)
        expected_new_fuel = 80
        self.assertEqual(self.vehicle.fuel, expected_new_fuel)

    def test_str_method(self):
        expected_str = f"The vehicle has 100 " \
                       f"horse power with 12 fuel left and 1.25 fuel consumption"
        self.assertEqual(self.vehicle.__str__(), expected_str)
