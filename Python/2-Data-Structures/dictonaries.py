# dictonaries are a collection of key value pairs

# you can define a dictonary like this:
poin = {"x": 1, "y": 2}
# or by using the dict() with keyword arguments
point = dict(x=1, y=2)
# indexes are the name of the keys
print(point["x"])
point["x"] = 1111
point["z"] = 9090
print(point)
# to avoid errors, check first
if "a" in point:
    print(point["a"])
# or use the get method which taakes the second arguments as
# your statement. In this case we want to return 0
print(point.get("a", 0))
del point["x"]
print(point)


# loop over dictonaries
for key in point:
    print(key, point[key])
# or
for key, value in point.items():
    print(key, value)
# this last method returns a tuple which can be unpacked


# dictonary comprehensions
values = []
for x in range(5):
    values.append(x * 2)

# however, we can use either a map or comprehension to
# make it cleaner
myList = [x * 2 for x in range(5)]  # <- list
print(type(myList))
print(myList)
mySet = {x * 2 for x in range(5)}  # <- set
print(type(mySet))
print(mySet)
myDic = {x: x * 2 for x in range(5)}  # <- dic
print(type(myDic))
print(myDic)
