

class Rectangle:
    def __init__(self, x, y, width, height):
        'Initialize a Rectangle instance with position and dimensions.'
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def area(self):
        'Calculate and return the area of the rectangle.'
        return self.width * self.height

    @property
    def perimeter(self):
        'Calculate and return the perimeter of the rectangle.'
        return 2 * (self.width + self.height)

    @property
    def pos_x(self):
        'Return the x-coordinate of the rectangle.'
        return self.x

    @property
    def pos_y(self):
        'Return the y-coordinate'
        return self.y

    def translate(self, dx, dy):
        'Move the rectangle by dx and dy.'
        self.x += dx
        self.y += dy

    def is_point_inside(self, point_x, point_y):
        'Check if a point is inside the rectangle.'
        return (
            self.x <= point_x <= self.x + self.width and
            self.y <= point_y <= self.y + self.height
        )

    def is_square(self):
        'Check if the rectangle is a square.'
        return self.width == self.height

    def __eq__(self, other):
        'Check if two rectangles have the same area.'
        return self.area == other.area

    def __lt__(self, other):
        'Check if the rectangle has a smaller area than another rectangle.'
        return self.area < other.area

    def __gt__(self, other):
        'Check if the rectangle has a larger area than another rectangle.'
        return self.area > other.area

    def __le__(self, other):
        'Check if the rectangle has a smaller or equal area than another rectangle.'
        return self.area <= other.area

    def __ge__(self, other):
        'Check if the rectangle has a larger or equal area than another rectangle.'
        return self.area >= other.area

    def __repr__(self):
        'Return the formal string representation of the rectangle.'
        return f"Rectangle:x={self.x},y={self.y}, " \
               f"width={self.width}, height={self.height})"

    def __str__(self):
        'Return the informal string representation of the rectangle.'
        return f"Rectangle (Position=(x={self.x}, Position=(y={self.y}), Width={self.width}, " \
               f"Height={self.height}, Area={self.area}, Perimeter={self.perimeter}"
