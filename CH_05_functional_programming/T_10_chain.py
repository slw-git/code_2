import itertools

a = range(3)
b = range(5)
print(list(itertools.chain(a, b)))
# [0, 1, 2, 0, 1, 2, 3, 4]
print(list(a)+list(b)+list(b))

iterables = [range(3), range(5), range(9)]
print(iterables)
print(list(itertools.chain.from_iterable(iterables)))
#[0, 1, 2, 0, 1, 2, 3, 4]
