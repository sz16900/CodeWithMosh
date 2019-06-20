for x in "Python":
    print(x)

print("")

for x in ['a', 'b', 'c']:
    print(x)

print("")

for x in range(0, 10, 2):
    print(x)

print("")

print(type(range(500000)))
print(1, 2, 3, 5, 55)

# for...else

names = ["AJohn", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not found")


# While

guess = 0
answer = 5
while answer != guess:
    guess = int(input("Guess: "))
else:
    pass
