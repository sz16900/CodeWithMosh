# are read onlt list, cannot be modified...
# tuples are ussed to prevent from deleting or adding items
# its a way of keeping things safe

point = (1, 2)
# or point = 1,2
print(point)
point = point + (3, 4)
print(point)
point = point * 3
print(point)
# to conver a list to a tuple
point = [1, 2]
print(type(point))
point = tuple(point)
print(type(point))
chars = tuple("hello world!")
# because tuples are iterable
print(chars)
point = (1, 2, 3)
# unpack tuple
x, y, z = point
print(x, y, z)

# swapping variables
# its easily done with tuples and unpacking

x = 11
y = 12
# because we are unpacking a tuple into two variables :)
x, y = y, x
