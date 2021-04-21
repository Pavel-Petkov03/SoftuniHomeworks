import functools


def even_parameters(function):
    functools.wraps(function)

    def wrapper(*args):
        try:
            f = function(*args)
            if f % 2 != 0:
                return "Please use only even numbers!"
            return f(*args)
        except TypeError:
            return "Please use only even numbers!"

    return wrapper

@even_parameters
def emp():
    return 'hi'

print(emp)

