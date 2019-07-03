# a cleaner and better permormant way of using maps
# and filters

items = [
    ("product1", 99),
    ("product11", 995),
    ("product12", 996),
    ("product134", 899),
]


# prices = list(map(lambda item: item[1], items))
# ^ this is too noisy try this instead:
# [expression for item in items]
prices = [item[1] for item in items]

# x = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
print(prices)
print(filtered)


# zip
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list(zip(list1, list2)))


#
