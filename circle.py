import math
class Circle:
    def __init__(self, x, y, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive value.")
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    @property
    def center_x(self):
        return self.x

    @property
    def center_y(self):
        return self.y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def is_point_inside(self, point_x, point_y):
        return math.sqrt((point_x - self.x) ** 2 + (point_y - self.y) ** 2) <= self.radius

    def is_unit_circle(self):
        return math.isclose(self.radius, 1)

    def __eq__(self, other):
        return math.isclose(self.radius, other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __repr__(self):
        return f"(x={self.x}, y={self.y}, radius={self.radius})"

    def __str__(self):
        return (f"(x={self.x}, y={self.y}), "
                f"Radius={self.radius}, "
                f"Area={self.area}, "
                f"Circumference={self.circumference}")
