import math

class Circle:
    def __init__(self, x, y, radius):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or not isinstance(radius, (int, float)):
            raise TypeError("ValueError x, y, and radius must be numbers.")
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    @property
    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.radius

    @property
    def center_x(self):
        """Return the x-coordinate of the center of the circle."""
        return self.x

    @property
    def center_y(self):
        """Return the y-coordinate of the center of the circle."""
        return self.y

    def translate(self, dx, dy):
        """Validate that dx and dy are numbers.
        Move the circle by dx and dy."""
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("dx and dy must be numbers.")

        # Move the circle by dx and dy.
        self.x += dx
        self.y += dy

    def is_inside(self, point_x, point_y):
        """Check if a point is inside the circle.
        validates."""
        if not isinstance(point_x, (int, float)) or not isinstance(point_y, (int, float)):
            raise TypeError("point_x and point_y must be numbers.")
        return math.sqrt((point_x - self.x) ** 2 + (point_y - self.y) ** 2) <= self.radius


    def __eq__(self, other):
        """Check if two circles have the same position and radius."""
        return math.isclose(self.radius, other.radius)

    def __lt__(self, other):
        """Check if the circle has a smaller area than another circle."""
        return self.area < other.area

    def __gt__(self, other):
        """Check if the circle has a larger area than another circle."""
        return self.area > other.area

    def __le__(self, other):
        """Check if the circle has a smaller or equal area than another circle."""
        return self.area <= other.area

    def __ge__(self, other):
        """Check if the circle has a larger or equal area than another circle."""
        return self.area >= other.area

    def __repr__(self):
        """Return repr string representation of the circle."""
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, radius={self.radius})"

    def __str__(self):
        """Return str string representation of the circle."""
        return (f"(x={self.x}, y={self.y}), "
                f"Radius={self.radius}, "
                f"Area={self.area}, "
                f"Circumference={self.circumference}")
