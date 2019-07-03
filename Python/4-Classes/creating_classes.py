# All Objects should have at least one parameters which we can cal self
# Objects are dynamic in Python


class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))
