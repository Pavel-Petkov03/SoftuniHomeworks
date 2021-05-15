import unittest
from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware


class HardwareTests(unittest.TestCase):
    def setUp(self):
        self.hard = Hardware('name', 'type', 12, 12)
        self.light = LightSoftware('l', 15, 15)

    def test_init_(self):
        self.assertEqual(self.hard.name, 'name')
        self.assertEqual(self.hard.type, 'type')
        self.assertEqual(self.hard.memory, 12)
        self.assertEqual(self.hard.capacity, 12)
        self.assertEqual(self.hard.software_components, [])

    def test_install_func_with_bigger_memory_consumption_expected_error(self):
        self.light.capacity_consumption = 0
        with self.assertRaises(Exception) as ex:
            self.hard.install(self.light)
            self.assertEqual(ex.exception, "Software cannot be installed")

    def test_install_func_with_bigger_capacity_consumption_expected_error(self):
        self.light.memory_consumption = 0
        with self.assertRaises(Exception) as ex:
            self.hard.install(self.light)
            self.assertEqual(ex.exception, "Software cannot be installed")

    def test_install_func_with_equal_capacity_consumption_and_equal_memory_append(self):
        self.light.capacity_consumption = 12
        self.light.memory_consumption = 12
        self.hard.install(self.light)
        self.assertEqual(self.hard.software_components, [self.light])

    def test_install_func_append_software(self):
        self.light.capacity_consumption = 0
        self.light.memory_consumption = 0
        self.hard.install(self.light)
        self.assertEqual(self.hard.software_components, [self.light])


    def test_uninstall_expect_to_remove_software(self):
        self.light.capacity_consumption = 0
        self.light.memory_consumption = 0
        self.assertEqual(self.hard.software_components, [])
        self.hard.install(self.light)
        self.assertEqual(self.hard.software_components, [self.light])
        self.hard.uninstall(self.light)
        self.assertEqual(self.hard.software_components, [])



if __name__ == '__main__':
    unittest.main()


