class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        super().append(object)
        print("Append called")
        # calling the method of the super class
        # the append method of list to tweak it
        # we are not replacing the append method
        super().append(object)


list = TrackableList()
list.append("1")
