def increment(number, by):
    return (number, number + by)


# this is a tuppple which basically means read only
print(increment(3, 3))

# or you can define it by using a keyword argumenr (by=3) to make it more readable
print(increment(3, by=3))

# or default values


def increment2(number, by=1):
    return (number, number + by)


print(increment2(3))


# annotate as well

def increment3(number: int, by: int = 45) -> tuple:
    return (number, number + by)


print(increment3(3))


# xargs

def multiply(*list):
    print(list)   # <- this is a tuple
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


# xxargs

def save_user(**user):
    print(user)


save_user(id=1, name="john")
