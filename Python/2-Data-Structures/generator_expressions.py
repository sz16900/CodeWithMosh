# in situations where you are dealing with a huge data set
# begin using generator expressions
# they take a lot less memory because they are always generating

from sys import getsizeof

values = (x * 2 for x in range(500000))  # <- this takes a lot less memory
print("gen:", getsizeof(values))
values = [x * 2 for x in range(500000)]
print("list:", getsizeof(values))

# Remember:
# generator objects are not stored in memory, therefore we
# cannot get to an specific object or we cant find the length
values = (x * 2 for x in range(500000))  # <- this takes a lot less memory
print(len(values))  # <- this throws an error
