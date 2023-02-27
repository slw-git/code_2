import operator
import itertools

# Sales per month
months = [10, 8, 5, 7, 12, 10, 5, 8, 15, 3, 4, 2]
print(list(itertools.accumulate(months, operator.add)))
print(list(itertools.accumulate(months)))
print(list(itertools.accumulate(months, operator.mul)))
# [10, 18, 23, 30, 42, 52, 57, 65, 80, 83, 87, 89]
