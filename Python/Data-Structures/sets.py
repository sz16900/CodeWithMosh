# sets use curly braces and dont repeat
# unordered collection of itwms, so cant access them using index


numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)
second = {5, 1}
second.add(9)
print(second)
second.remove(9)
print(second)
print(len(second))


first = set(numbers)

# use the vertical bar | to get a union of the first and second set
print("the union of two sets are: ", first | second)
# use & to find the intersection of two sets
print("the intersection of two sets are: ", first & second)
# use - to find the difference of two sets
print("the difference of two sets are: ", first - second)
# use ^ for symmetric difference of two sets
# this returns the items that are either in the first
# or second set but not both
print("the symmetric difference of two sets are: ", first ^ second)

# cant access them using indexing
# so you have to check if items exists. Example:
if 1 in first:
    print("yes")
