def tags(type_of_tag):
    def decorator(function):
        def wrapper(*args):
            return f'<{type_of_tag}>{function(*args)}</{type_of_tag}>'

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))


