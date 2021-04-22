class IntegerList:
    def __init__(self, list_of_ints):
        self.list_of_ints = list_of_ints

    @staticmethod
    def __validate_index(index, list_of_int):
        return 0 <= index < len(list_of_int)

    @staticmethod
    def __validate_type(t):
        return int is type(t)

    def add(self, el):
        if self.__validate_type(el):
            self.list_of_ints.append(el)
            return self.list_of_ints
        raise ValueError()

    def remove_index(self, index):
        if self.__validate_index(index, self.list_of_ints):
            return self.list_of_ints.pop(index)
        raise IndexError()

    def get(self, index):
        if self.__validate_index(index, self.list_of_ints):
            return self.list_of_ints[index]
        raise IndexError()

    def insert(self, index, element):
        if not self.__validate_type(element):
            raise ValueError()
        elif not self.__validate_index(index, self.list_of_ints):
            raise IndexError()

        self.list_of_ints.insert(index, element)

    def get_biggest(self):
        return max(self.list_of_ints)

    def get_index(self, element):
        if element in self.list_of_ints:
            return self.list_of_ints.index(element)


import unittest


class MyTest(unittest.TestCase):

    def setUp(self):
        self.list = IntegerList([1, 2, 3, 4, 5])

    def test_for_add_func_with_another_type__expected_error(self):
        with self.assertRaises(ValueError):
            self.list.add('12')

    def test_for_add_function_append_new_element(self):
        self.list.add(7)
        self.assertListEqual([1, 2, 3, 4, 5, 7], self.list.list_of_ints)

    def test_for_remove_index__index_not_in_range__expected_error(self):
        with self.assertRaises(IndexError):
            self.list.remove_index(6)

    def test_for_remove_index__expected_remove_the_current_index_and_return_the_result(self):
        expected = 1
        actual = self.list.remove_index(0)
        self.assertEqual(expected, actual)

    def test_get_element_by_index_from_the_list__expected_return_element(self):
        expected = 1
        actual = self.list.get(0)
        self.assertEqual(expected, actual)

    def test_get_index_in_list__index_not_in_range__expected_error(self):
        with self.assertRaises(IndexError):
            self.list.get(6)

    def test_insert_method_index_not_in_range__expected_index_error(self):
        with self.assertRaises(IndexError):
            self.list.insert(10, 2)

    def test_insert_method_el_not_int__expected__value_error(self):
        with self.assertRaises(ValueError):
            self.list.insert(0, True)

    def test_insert_method_everything_is_fine_and_insert_element_to_the_given_index(self):
        self.list.insert(0, 0)
        expected = [0, 1, 2, 3, 4, 5]
        self.assertListEqual(expected, self.list.list_of_ints)

    def test_get_biggest_expect_get_the_biggest_element_from_the_list(self):
        expected_max_el = 5
        self.assertEqual(expected_max_el, self.list.get_biggest())

    def test_get_index_if_el_in_list_and_return_element(self):
        actual_index = self.list.get_index(1)
        expected_index = 0
        self.assertEqual(expected_index, actual_index)


if __name__ == "__main___":
    unittest.main()
