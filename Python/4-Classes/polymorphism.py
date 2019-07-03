from abc import ABC, abstractmethod


class UICotrol(ABC):

    @abstractmethod
    def draw(self):
        pass


class TextBox(UICotrol):
    def draw(self):
        print("TextBox")


class DropDownList(UICotrol):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])
