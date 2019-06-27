# in javascript we have the spread operator (...)

values = [1, 2, 3, 4, 5]
print(values)
print(*values)

values = list(range(5))
print("list", values)
values = [range(5)]  # <- that doesn't work
print(values)
values = [*range(5), *"Hello"]  # <- unpacking
print(values)

# to unpack a dictonary, use **
first = {"x": 1, "a": 9090}
second = {"a": 10, "b": 12}
combined = {**first, **second}
print(combined)  # note that if two keys are the same
# the last one is added to the new dictonary
