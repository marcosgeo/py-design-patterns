# LSP: liskov substitution principle
"""
Whenever you have an interface taking some sort of base class,
you should be able to stkick in any of its inheritors
"""

class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    # THESE SETTERS ARE A VIOLATION OF THE PRINCIPLE
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

def use_it(rc):
    # THIS FUNCTION BREAKS THE LISKOV PRINCIPLE
    # SINCE IT CHANGE OBJETCS VALUES INSIDE OF IT
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f"Orig: Expected an area of {expected}, got {rc.area}")


def use_it_better(rc, expected):
    print(f"Better: Expected an area of {expected}, got {rc.area}")


if __name__ == "__main__":
    rc = Rectangle(5, 4)
    use_it(rc)
    rc = Rectangle(5, 4)
    use_it_better(rc, 20)

    sq = Square(5)
    use_it(sq)
    sq = Square(5)
    use_it_better(sq, 25)