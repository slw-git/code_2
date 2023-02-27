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

primes =  [0, 0, 1, 1, 0, 1, 0, 1]
odd =     [0, 1, 0, 1, 0, 1, 0, 1]
numbers = ['zero', 'one', 'two', 'three', 'four', 'five']

# Primes:
print(list(itertools.compress(numbers, primes)))
# ['two', 'three', 'five']

# Odd numbers
print(list(itertools.compress(numbers, odd)))
# ['one', 'three', 'five']

# Odd primes
# ...and...
print(list(itertools.compress(numbers, map(all, zip(odd, primes)))))
# ...or...
print(list(itertools.compress(numbers, map(any, zip(odd, primes)))))
# ['three', 'five']
