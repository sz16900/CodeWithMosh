name = " "

if not name.strip():
    print("Name is Empty")

age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")


# TERNARY OPERATOR

message = "Eligible Again" if age >= 18 else "Not Eligible"
print(message)
