import itertools

print(list(itertools.islice(itertools.count(), 10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(itertools.islice(itertools.count(), 5, 11, 1)))
# [5, 7, 9]

print(list(itertools.islice(itertools.count(10, 2.5), 5)))
# [10, 12.5, 15.0, 17.5, 20.0]
