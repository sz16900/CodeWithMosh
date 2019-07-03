# a list of tuples and how to sort them
# The ugly way
items = [
    ("product1", 99),
    ("product11", 995),
    ("product12", 996),
    ("product134", 899),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
# The pretty way by using Lambda functions
items = [
    ("product1", 99),
    ("product11", 995),
    ("product12", 996),
    ("product134", 899),
]
items.sort(key=lambda item: item[1])  # key=lambda parameter:expression
print(items)


# maps
items = [
    ("product1", 99),
    ("product11", 995),
    ("product12", 996),
    ("product134", 899),
]
# prices = []
# for item in items:
#     prices.append(item[1])
# <- we convert a map into a list because lists are iterable
prices = list(map(lambda item: item[1], items))
print(prices)


# filter
items = [
    ("product1", 12),
    ("product11", 3),
    ("product12", 10),
    ("product134", 5),
]

x = list(filter(lambda item: item[1] >= 10, items))
print(x)
