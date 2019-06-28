try:
    # with the with statement, we don't need to have a finally
    # clause because it automaticalle call a meta file called
    # __exit__ which will close the file which you just
    # opened
    with open("app.py") as file:
        print("file opened")

    age = int(input("age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Invalid age.")
else:
    print("Good! We can move on.")
