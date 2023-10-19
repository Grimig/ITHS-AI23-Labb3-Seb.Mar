
class Rectangle:
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        """
        Initialize a Rectangle instance with position and dimensions."""
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def area(self):
        """
        Calculate and return the area of the rectangle."""
        return self.width * self.height

    @property
    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle"""
        return 2 * (self.width + self.height)

    def translate(self, dx, dy):
        """
        Move the rectangle by dx and dy."""
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("dx and dy must be numbers.")
        self.x += dx
        self.y += dy

    def is_inside(self, point_x, point_y):
        """
        Check if a point is inside the rectangle."""
        if not isinstance(point_x, (int, float)):
            raise TypeError("point_x must be a number.")
        if not isinstance(point_y, (int, float)):
            raise TypeError("point_y must be a number.")
        return (
            self.x < point_x < self.x + self.width
            and self.y < point_y < self.y + self.height
        )

    def is_square(self):
        """
        Return True if the rectangle is a square."""
        return self.width == self.height


    def __eq__(self, other):
        """
        Check if two rectangles have the same area."""
        if not isinstance(other, Rectangle):
            raise TypeError("Comparison with non-Rectangle object.")
        return self.area == other.area

    def __lt__(self, other):
        """
        Check if the rectangle has a smaller area than another rectangle."""
        if not isinstance(other, Rectangle):
            raise TypeError("Comparison with non-Rectangle object.")
        return self.area < other.area

    def __gt__(self, other):
        """
        Check if the rectangle has a larger area than another rectangle."""
        if not isinstance(other, Rectangle):
            raise TypeError("Comparison with non-Rectangle object.")
        return self.area > other.area

    def __le__(self, other):
        """
        Check if the rectangle has a smaller or equal area than another rectangle."""
        if not isinstance(other, Rectangle):
            raise TypeError("Comparison with non-Rectangle object.")
        return self.area <= other.area

    def __ge__(self, other):
        """
        Check if the rectangle has a larger or equal area than another rectangle."""
        if not isinstance(other, Rectangle):
            raise TypeError("Comparison with non-Rectangle object.")
        return self.area >= other.area

    def __repr__(self):
        """Return repr string representation of the rectangle."""
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def __str__(self):
        """
        Return str string representation of the rectangle."""
        return (
            f"{self.__class__.__name__}(x={self.x}, y={self.y}), "
            f"Width={self.width}, Height={self.height}, "
            f"Area={self.area}, Perimeter={self.perimeter})"
        )
