class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self):
        self.my_list = IntegerList(1, 2, 3, 4)

    def test_add_function_element__with_not_int_element__expected_value_error(self):
        with self.assertRaises(ValueError):
            self.my_list.add('12')

    def test_add_function_with_int_element__expected_append_to_list_and_return_the_whole_list(self):
        self.my_list.add(5)
        expected = self.my_list.get_data()
        actual = [1, 2, 3, 4, 5]
        self.assertListEqual(expected, actual)

    def test_remove_index_index_greater_than_len_of_list__expected_index_out_of_range_error(self):
        with self.assertRaises(IndexError):
            self.my_list.remove_index(10)

    def test_remove_valid_index_and_return_the_element_from_the_index_and_remove_it(self):
        actual_return = self.my_list.remove_index(0)
        expected_return = 1
        expected_final_list = [2, 3, 4]
        self.assertEqual(expected_return, actual_return)
        self.assertListEqual(self.my_list.get_data(), expected_final_list)

    def test_get_function_with_invalid_index__expected_index_error(self):
        with self.assertRaises(IndexError):
            self.my_list.get(10)

    def test_get_function_with_valid_index__expected_element_from_index_in_the_list(self):
        expected = 0
        actual = self.my_list.get_index(1)
        self.assertEqual(expected, actual)

    def test_insert_function_with_invalid_index__expected_index_out_of_range_error(self):
        with self.assertRaises(IndexError):
            self.my_list.insert(10, 5)

    def test_insert_function_with_invalid_type__expected_value_error(self):
        with self.assertRaises(ValueError):
            self.my_list.insert(0, '12')

    def test_insert_function_everything_is_valid__insert_el_to_the_given_index(self):
        expected_final_list = [1, 2, 3, 12, 4]
        self.my_list.insert(3, 12)

        self.assertListEqual(expected_final_list, self.my_list.get_data())

    def test_get_biggest_function_expected_biggest_element(self):
        expected_max_element = 4
        actual_max = self.my_list.get_biggest()
        self.assertEqual(expected_max_element, actual_max)

    def test_get_index_function_expected_return_element_to_the_given_index(self):
        expected = 3
        actual = self.my_list.get_index(4)
        self.assertEqual(expected, actual)


if __name__ == "__main___":
    unittest.main()

