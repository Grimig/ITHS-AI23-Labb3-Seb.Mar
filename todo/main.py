
from rectangle import Rectangle
from circle import Circle

def print_header(title):
    print("\n" + "="*30)
    print(f"{title.center(30)}")
    print("="*30)

def rectangle_menu():
    print_header("Rectangle Operations")
    x = float(input("Enter x-coordinate of the rectangle: "))
    y = float(input("Enter y-coordinate of the rectangle: "))
    width = float(input("Enter width of the rectangle: "))
    height = float(input("Enter height of the rectangle: "))
    rect = Rectangle(x, y, width, height)
    while True:
        print_header("Rectangle Menu")
        print("1. Display Rectangle Properties")
        print("2. Translate Rectangle Position")
        print("3. Check if a Point is Inside the Rectangle")
        print("4. Check if the Rectangle is a Square")
        print("5. Exit to Main Menu")
        choice = input("Select an option (1-5): ")
        if choice == '1':
            print(f"\nArea: {rect.area}, Perimeter: {rect.perimeter}")
        elif choice == '2':
            dx = float(input("Enter the x-distance to translate: "))
            dy = float(input("Enter the y-distance to translate: "))
            rect.translate(dx, dy)
            print(f"New Position: ({rect.x}, {rect.y})")
        elif choice == '3':
            px = float(input("Enter x-coordinate of the point: "))
            py = float(input("Enter y-coordinate of the point: "))
            print(f"Is the Point Inside: {rect.is_inside(px, py)}")
        elif choice == '4':
            print(f"Is it a Square: {rect.is_square}")
        elif choice == '5':
            break
        else:
            print("Invalid selection. Please try again.")

def circle_menu():
    print_header("Circle Operations")
    x = float(input("Enter x-coordinate of the circle: "))
    y = float(input("Enter y-coordinate of the circle: "))
    radius = float(input("Enter radius of the circle: "))
    circle = Circle(x, y, radius)
    while True:
        print_header("Circle Menu")
        print("1. Display Circle Properties")
        print("2. Translate Circle Position")
        print("3. Check if a Point is Inside the Circle")
        print("4. Check if the Circle is a Unit Circle")
        print("5. Exit to Main Menu")
        choice = input("Select an option (1-5): ")
        if choice == '1':
            print(f"\nArea: {circle.area}, Circumference: {circle.circumference}")
        elif choice == '2':
            dx = float(input("Enter the x-distance to translate: "))
            dy = float(input("Enter the y-distance to translate: "))
            circle.translate(dx, dy)
            print(f"New Position: ({circle.x}, {circle.y})")
        elif choice == '3':
            px = float(input("Enter x-coordinate of the point: "))
            py = float(input("Enter y-coordinate of the point: "))
            print(f"Is the Point Inside: {circle.is_inside(px, py)}")
        elif choice == '4':
            print(f"Is it a Unit Circle: {circle.is_unit_circle}")
        elif choice == '5':
            break
        else:
            print("Invalid selection. Please try again.")

def main():
    while True:
        print_header("Main Menu")
        print("1. Perform Rectangle Operations")
        print("2. Perform Circle Operations")
        print("3. Exit Program")
        choice = input("Select an option (1-3): ")
        if choice == '1':
            rectangle_menu()
        elif choice == '2':
            circle_menu()
        elif choice == '3':
            print("\nThank you for using the Geometry Program! Goodbye!\n")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
