class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.len = length

    def area(self):
        Shape.__init__(self)
        return self.len * self.len

aSquare = Square(3)
print(aSquare.area())

