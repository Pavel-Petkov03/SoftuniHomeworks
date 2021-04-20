import functools


def make_bold(function):
    functools.wraps(function)

    def wrapper(*args):
        result = f'<b>{function(*args)}</b>'
        return result

    return wrapper


def make_italic(function):
    functools.wraps(function)

    def wrapper(*args):
        result = f'<i>{function(*args)}</i>'
        return result

    return wrapper


def make_underline(function):
    functools.wraps(function)

    def wrapper(*args):
        result = f'<u>{function(*args)}</u>'
        return result

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
