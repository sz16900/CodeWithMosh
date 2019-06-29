class Point:
    # Below is an example of a Class attribute
    default_color = "red"

    # self is a reference to the current Point object
    def __init__(self, x, y):  # <- constructor

        # below are instance attributes
        self.x = x
        self.y = y

    @classmethod  # <- decorator
    def zero(cls):  # <- cls = class which is a reference to a class itself. This is only a convention

    def draw(self):
        print(f"Point: ({self.x}, {self.y})")


# Note this changes the attributes
Point.default_color = "yellow"

point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.draw()
