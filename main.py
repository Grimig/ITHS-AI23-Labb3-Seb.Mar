from rectangle import Rectangle
from circle import Circle

def main():
    # Create Rectangle instances
    rect1 = Rectangle(2, 0, 4, 5)
    rect2 = Rectangle(0, 1, 4, 5)

    # Demonstrate Rectangle methods and properties
    print(f"Rectangle 1: {rect1}")
    print(f"Rectangle 2: {rect2}")
    print(f"Area of Rectangle 1: {rect1.area}")
    print(f"Perimeter of Rectangle 1: {rect1.perimeter}")
    print(f"Is Rectangle 1 equal to Rectangle 2: {rect1 == rect2}")
    print(f"Is point (2, 2) inside Rectangle 1: {rect1.is_inside(2, 2)}")
    print(f"Is Rectangle 1 a square: {rect1.is_square()}")

    # Translate Rectangle 1
    rect1.translate(3, 3)
    print(f"Rectangle 1 after translation: {rect1}")

    # Create Circle instances
    circle1 = Circle(0, 0, 1)
    circle2 = Circle(0, 0, 2)

    # Demonstrate Circle methods and properties
    print(f"\nCircle 1: {circle1}")
    print(f"Circle 2: {circle2}")
    print(f"Area of Circle 1: {circle1.area}")
    print(f"Circumference of Circle 1: {circle1.circumference}")
    print(f"Is Circle 1 equal to Circle 2: {circle1 == circle2}")
    print(f"Is point (0.5, 0.5) inside Circle 1: {circle1.is_inside(0.5, 0.5)}")
    print(f"Is Circle 1 a unit circle: {circle1.is_unit_circle()}")

    # Translate Circle 1
    circle1.translate(3, 3)
    print(f"Circle 1 after translation: {circle1}")

    print("Done.")
if __name__ == "__main__":
    main()
