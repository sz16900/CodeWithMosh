try:
    age = int(input("age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Invalid age.")
else:
    print("Good! We can move on.")

#################################
