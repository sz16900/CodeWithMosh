class Point:
    # self is a reference to the current Point object
    def __init__(self, x, y):  # <- constructor
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point: ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
