import functools


def type_check(my_type):
    functools.wraps(my_type)

    def decorator(function):
        def wrapper(arg):
            if my_type is type(arg):
                return function(arg)
            return 'Bad Type'

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
