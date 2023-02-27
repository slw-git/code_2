def add_value_functional(items, value):
    return items + [value]


def add_value_regular(items, value):
    items.append(value)
    return items


items = [1, 2, 3]
items_2 = add_value_functional(items, 5)
print(f'func: {items}')
print(f'func 2: {items_2}')

add_value_regular(items, 5)
print(f'reg: {items}')

