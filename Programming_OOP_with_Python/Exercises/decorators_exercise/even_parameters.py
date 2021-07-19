import functools


def even_parameters(function):
    functools.wraps(function)

    def wrapper(*args):
        try:
            f = function(*args)
            if len([el for el in args if el % 2 == 0]) != len(args):
                return "Please use only even numbers!"
            return f
        except TypeError:
            return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(4, 2))
