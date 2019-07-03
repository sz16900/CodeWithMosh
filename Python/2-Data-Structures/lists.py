letters = ["a", "b", "c"]
matrix = [[1, 2], [3, 4]]
zeros = [0] * 5
combined = zeros + letters
print(combined)
numbers = list(range(20))  # <- lists are iterable
print(numbers)
chars = list("Hello World!")
print(chars)

new_numbers = list(range(20))
print(new_numbers[::2])  # <- slicing and stepping over 2
print(new_numbers[::-2])


# List packing and unpacking
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, *other, last = numbers_list
print(first, second, last)
print(other)


# enumerate: always returns a tuple (read-only)
# with enumerate you can unpack the contents straight after the for loop keyword
letterss = ["a", "b", "c"]
for index, letter in enumerate(letterss):
    print(index, letter)


# add
letters.append("d")
letters.insert(0, "-")
# remove
letters.pop(0)
letters.remove("b")
# if want to remove more than one "b", loop over to remove all of them
del letters[0:3]  # removes a range of items
letters.clear()  # clears the whole list
print(letters)


# finding items
letters = ["a", "b", "c"]
print(letters.index("a"))
if "d" in letters:  # use this to avoid errors
    print(letters.index("d"))

# count
print(letters.count("d"))


# sorting lists
num = [1, 2, 44, 5, 6, 88, 0]
num.sort(reverse=True)
print(num)
num.sort()
print(num)
num = [1, 2, 44, 5, 6, 88, 0]
# doesnt modify the original list, it returns a new list
print(sorted(num, reverse=True))
print(num)
