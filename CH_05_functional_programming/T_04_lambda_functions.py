import operator

values = dict(one=1, two=2, three=3)
print(sorted(values.items()))
# [('one', 1), ('three', 3), ('two', 2)]
print(sorted(values.items(), key=(lambda item: item[1])))
# [('one', 1), ('two', 2), ('three', 3)]

get_value = operator.itemgetter(1)
print(sorted(values.items(), key=get_value))
# [('one', 1), ('two', 2), ('three', 3)]
