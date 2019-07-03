def fizzbuzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "fizzbuzz"
    if number % 3 == 0:
        return "fizz"
    if number % 5 == 0:
        return "buzz"
    return number


for x in range(1, 100):
    print(fizzbuzz(x))
