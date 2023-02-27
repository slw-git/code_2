import operator
import functools


def rreduce(function, iterable):
    print(f'iterable={iterable}')
    # Fetch the first item to prime `result`
    result, *iterable = iterable

    for item in iterable:
        old_result = result
        result = function(result, item)
        print(f'{old_result} * {item} = {result}')

    return result


print('T_07')
r = range(1, 6)
print(list(r))
print(functools.reduce(operator.mul, r))
print(functools.reduce(operator.add, r))
# 24

rreduce(operator.mul, r)