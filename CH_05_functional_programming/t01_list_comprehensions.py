import os


def square(x):
    return x ** 2


def odd(x):
    return x % 2


squares = [x ** 2 for x in range(10)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ------------------------------------------------------------------------------

odd_squares = [x ** 2 for x in range(10) if x % 2]
print(odd_squares)
# [1, 9, 25, 49, 81]

# ------------------------------------------------------------------------------

squares = list(map(square, range(10)))
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

odd_squares = list(filter(odd, map(square, range(10))))
print(odd_squares)
# [1, 9, 25, 49, 81]

# ------------------------------------------------------------------------------

directories = filter(os.path.isdir, os.listdir('.'))
print(f'2: {directories}')

# Versus:

directories = [x for x in os.listdir('.') if os.path.isdir(x)]
print(f'2: {directories}')

# ------------------------------------------------------------------------------
print([x // 2 for x in range(3)])
# Set comprehension
numbers = {x // 2 for x in range(3)}
print(sorted(numbers))

# ------------------------------------------------------------------------------
print({x: x ** 2 for x in range(6)})
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print( {x: x ** 2 for x in range(6) if x % 2})
# {1: 1, 3: 9, 5: 25}
