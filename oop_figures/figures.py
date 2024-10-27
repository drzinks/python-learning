class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def count_surface(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


class Cube():
    def __init__(self, square: Square):
        self.base = square #aggregation not inheritance

    def count_surface(self):
        return 6 * self.base.count_surface()

    def count_volume(self):
        return self.base.count_surface() * self.base.width

cube = Cube(Square(2))
rectangle = Rectangle(2,3)
square = Square(2)

print(square.count_surface())
print(rectangle.count_surface())
print(cube.count_surface())
print(cube.count_volume())
