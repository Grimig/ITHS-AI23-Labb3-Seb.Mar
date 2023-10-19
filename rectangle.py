
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    @property ##plotlib?
    def pos_x(self):
        return self.x

    @property #plotlib?
    def pos_y(self):
        return self.y

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __le__(self, other):
        return self.area <= other.area

    def __ge__(self, other):
        return self.area >= other.area

    def __repr__(self):
        # Implement the representation of the object.
        return f"""
        Rectangle: (x={self.x}, y={self.y},
        width={self.width}, height={self.height})
        """

    def __str__(self):
        # Implement the string representation of the object.
        return f"Rectangle (x={self.x}, y={self.y}), Width={self.width}, Height={self.height}, Area={self.area}, Perimeter={self.perimeter}"

    def translate(self, dx, dy):
        # Method to move the x and y coordinates by dx and dy.
        self.x += dx
        self.y += dy
