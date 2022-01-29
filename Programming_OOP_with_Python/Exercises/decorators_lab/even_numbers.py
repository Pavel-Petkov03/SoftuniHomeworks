# def even_numbers(func):
#     def wrapper(*args, **kwargs):
#         return [x for x in func(*args, **kwargs) if x % 2 == 0]
#
#     return wrapper
#
#
# @even_numbers
# def get_numbers(numbers):
#     return numbers
#
#
# print(get_numbers([1, 2, 3, 4, 5]))


def timer(function):
    def inner(*args, **kwargs):
        begin = time.time()
        function(*args, **kwargs)
        end = time.time()
        return f"The total amount of time is {end - begin}"

    return inner


class Calculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def add(self):
        return self.first_number + self.second_number

    @timer
    def find_add_time(self):
        return self.first_number + self.second_number

