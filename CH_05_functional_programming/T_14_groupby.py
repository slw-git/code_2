import operator
import itertools

words = ['dd', 'aa', 'ab', 'ba', 'bb', 'ca', 'cb', 'cc']
words1 = ['a1', 'a1', 'b2', 'b2', 'c3', 'c3', 'c3']
words2 = ['a11', 'a11', 'b21', 'b22', 'c31', 'c31', 'c32']

# Gets the first element from the iterable
getter = operator.itemgetter(0)
getter1 = operator.itemgetter(1)
getter2 = operator.itemgetter(2)

for group, items in itertools.groupby(words, key=getter):
     print(f'group: {group}, items: {list(items)}')

for group, items in itertools.groupby(words1, key=getter1):
     print(f'(1) group: {group}, items: {list(items)}')

for group, items in itertools.groupby(words2, key=getter2):
     print(f'(2) group: {group}, items: {list(items)}')

"""
group: a, items: ['aa', 'ab']
group: b, items: ['ba', 'bb']
group: c, items: ['ca', 'cb', 'cc']
"""

raw_items = ['spam', 'eggs', 'sausage', 'spam']

def keyfunc(group):
     return group[0]

for group, items in itertools.groupby(raw_items, key=keyfunc):
     print(f'1_group: {group}, items: {list(items)}')
"""
group: s, items: ['spam']
group: e, items: ['eggs']
group: s, items: ['sausage', 'spam']
"""

raw_items.sort()
for group, items in itertools.groupby(raw_items, key=keyfunc):
     print(f'2_group: {group}, items: {list(items)}')
"""
group: e, items: ['eggs']
group: s, items: ['sausage', 'spam', 'spam']
"""