class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return (f'{self.name} has saved {self.money} money.')


import unittest


class WorkerTests(unittest.TestCase):
    name = 'Pavel'
    salary = 150
    energy = 100

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_check_for_valid_name__energy__salary(self):
        """
        Test if the worker is initialized with correct name, salary and energy
        """
        self.assertEqual(self.energy, self.worker.energy)
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)

    def test_check_for_worker__energy_increment_after_rest_method(self):
        """
        Test if the worker's energy is incremented after the rest method is called
        """
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_check_for_invalid_energy_expected_error(self):
        """
        Test if an error is raised if the worker tries to work with negative energy or equal to 0
        """
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_for_money_increase_after_work_method(self):
        """
        Test if the worker's money is increased by his salary correctly after the work method is called
        """
        self.worker.work()
        self.assertEqual(self.worker.money, self.salary)

    def test_check_for_energy_decrement_after_work_method(self):
        """
        Test if the worker's energy is decreased after the work method is called
        """
        self.worker.work()
        self.assertEqual(self.worker.energy, self.energy - 1)

    def test_get_info_method(self):
        """
        Test if the get_info method returns the proper string with correct values
        """
        expected = f'{self.name} has saved 0 money.'
        self.assertEqual(self.worker.get_info(), expected)


if __name__ == "__main__":
    unittest.main()
