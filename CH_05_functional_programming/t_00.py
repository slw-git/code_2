def add_value_functional(items, value):
     return items + [value]

items = [1, 2, 3]
add_value_functional(items, 5)
print(items)

def add_value_regular(items, value):
     items.append(value)
     return items

add_value_regular(items, 5)
print(items)

