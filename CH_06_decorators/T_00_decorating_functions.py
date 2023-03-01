def decorator(function):
    return function


def add(a, b):
    return a + b


add = decorator(add)


@decorator
def add(a, b):
    return a + b

