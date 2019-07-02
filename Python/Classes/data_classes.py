# Remember: if your classes dont have any behaviours (methods)
# but only data, then it probably is a good idea to use namedtuple
# However, namedtuples are not mutable, so in order to modify a value
# a new point needs to be created

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
# if want to modify
p1 = Point(x=11, y=12)
p2 = Point(x=1, y=2)
print(p1 == p2)
