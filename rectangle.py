
class Rectangle:
    def __init__(self, x, y, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
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
    def position_x(self):
        return self.x

    @property #plotlib?
    def position_y(self):
        return self.y

    def translate(self, dx, dy):
        # Method to move the x and y coordinates by dx and dy.
        self.x += dx
        self.y += dy

    def is_point_inside(self, point_x, point_y):
        # Method to check if a point (point_x, point_y) is inside the shape.
        return (
            self.x <= point_x <= self.x + self.width and
            self.y <= point_y <= self.y + self.height
        )

    def is_unit_circle(self):
        # Method to check if the shape is a unit circle (circle with radius 1).
        return self.width == self.height == 2

    def is_square(self):
        # Method to check if the shape is a square (width and height are equal).
        return self.width == self.height

    def __eq__(self, other): #equality
        return self.area == other.area

    def __lt__(self, other): #less than
        return self.area < other.area

    def __gt__(self, other): #greater than
        return self.area > other.area

    def __le__(self, other): #less than
        return self.area <= other.area

    def __ge__(self, other): #greater than
        return self.area >= other.area

    def __repr__(self): #representation
        return f"Rectangle: (Position: x={self.x}, Position: y={self.y}, width={self.width}, height={self.height})"

    def __str__(self): #string representation
        return f"Rectangle (x={self.x}, y={self.y}), Width={self.width}, Height={self.height}, Area={self.area}, Perimeter={self.perimeter}"
