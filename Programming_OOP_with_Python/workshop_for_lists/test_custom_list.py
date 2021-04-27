import unittest
from Programming_OOP_with_Python.workshop_for_lists.custom_list import CustomList


class CustomListTests(unittest.TestCase):
    def test_append__expected_return_of_list(self):
        pass

    def test_remove_index_expected__list_with_removes_value(self):
        pass

    def test_remove_index_with_invalid_index__expected_index_error(self):
        pass

    def test_get_index__expected_the_value_of_the_given_index(self):
        pass

    def test_get_index_with_invalid_index__expected_index_error(self):
        pass

    def test_extend_method_with_not_iterable_object__expected_custom_error(self):
        pass

    def test_extend_function_with_iterable_object__expected_new_list(self):
        pass

    def test_insert_function_with_invalid_index__expected_index_error(self):
        pass

    def test_insert_function__expected_new_list(self):
        pass

    def test_pop_function_with_invalid_index__expected_index_error(self):
        pass

    def test_pop_function__expected_popped_value(self):
        pass

    def test_clear_function__returns_empty_list_8_bits_len(self):
        pass

    def test_index_function_with_not_found_value__expected__custom_not_found_error(self):
        pass

    def test_index_function__expected_return_the_index_of_the_FIRST_VALUE(self):
        pass

    def test_count_function__expected_count_of_value(self):
        pass

    def test_reverse_returns_reversed_list_but_not_changing_the_instance(self):
        pass

    def test_copy_func_returns_not_instanced_copy_of_list(self):
        pass

    def  test_size__expected_return_the_size_of_the_list(self):
        pass

    def test_add_first__expected_changed_list(self):
        pass

    def test_dictionaries(self):
        pass

    def test_move_amount__expected_to_move_the_amount_of_values_to_the_end_of_the_list(self):
        pass

    def test_sum(self):
        pass

    def test_overbound(self):
        pass

    def test_underbound(self):
        pass


if __name__ == '__main__':
    unittest.main()

"""
        •	append(value) - Adds a value to the end of the list. Returns the list.
        •	remove(index) - Removes the value on the index. Returns the value removed.
        •	get(index) - Returns the value on the index.
        •	extend(iterable) - Appends the iterable to the list. Returns the new list.
        •	insert(index, value) - Adds the value on the specific index. Returns the list.
        •	pop() - Removes the last value and returns it.
        •	clear() - Removes all values, contained in the list.
        •	index(value) - Returns the index of the given value.
        •	count(value) - Returns the number of times the value is contained in the list.
        •	reverse() - Returns the values of the list in reverse order.
        •	copy() - Returns a copy of the list.

        We will also add our own custom functionalities:
        •	size() - Returns the length of the list.
        •	add_first(value) - Adds the value at the beginning of the list
        •	dictionize() - Returns the list as a dictionary: The keys will be each value on an even position and their values will be each value on an odd position. If the last value on an even position, it’s value will be " " (space)
        •	move(amount) - Move the first "amount" of values to the end of the list. Returns the list.
        •	sum() - Returns the sum of the list. If the value is not a number, add the length of the value to the overall number.
        •	overbound() - Returns the index of the biggest value. If the value is not a number, check it’s length.
        •	underbound() - Returns the index of the smallest value. If the value is not a number, check it’s length.

        Do not inherit List. Feel free to implement your own functionality (and unit tests) or to write the methods by yourself.
"""
