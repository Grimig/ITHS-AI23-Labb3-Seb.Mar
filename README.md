# ITHS-AI23-Labb3-Seb.Mar

# Geometri OOP

## Purpose

The purpose of this lab is to practice Object-Oriented Programming (OOP) in Python by designing a well-structured program. You will start by planning your class structure using UML and then implement it in Python.

## Task
create the following geometric classes:

- Rectangle
- Circle

**Note**: You may also need additional classes if you wish to utilize inheritance and/or composition.

### Class Requirements

#### Common Requirements for All Classes

- `area` property: To calculate the area of the shape.
- `circumference` property: To calculate the circumference or perimeter of the shape.
- `__eq__` method: To overload the `==` operator for equality checks.
- `__lt__`, `__gt__`, `__le__`, `__ge__` methods: To overload comparison operators for comparisons.
- `__repr__` method: To provide a formal string representation of the object.
- `__str__` method: To provide an informal string representation of the object.
- `x` and `y` attributes: To represent the center position of the object.
- `translate` method: To move the `x` and `y` positions.
- `contains_point` method: To check if a given point is inside the object.

#### Specific Requirements

##### For Circle

- `is_unit_circle` method: To check if the circle instance is a unit circle.

##### For Rectangle

- `is_square` method: To check if the rectangle instance is a square.

### Additional Features

Feel free to add more functionalities that fit, such as drawing the geometric shapes and visualizing translations.

Your classes should be in a `.py` file. They should be usable in the following manner:

```python
# Example usage

rectangle = Rectangle(x=0, y=0, width=10, height=20)

circle = Circle(x=0, y=0, radius=5)
