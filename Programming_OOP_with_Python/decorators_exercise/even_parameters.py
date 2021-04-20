import functools


def even_parameters(function):
    functools.wraps(function)

    def wrapper(*args):
        for arg in args:
            if type(arg) is not str and arg % 2 != 0:
                return "Please use only even numbers!"
        return function(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
