import math

class Shape:
    def area(self):
        """Method to be overridden by derived classes."""
        raise NotImplementedError("The area method must be overridden in subclasses.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Constructor: Initializes a Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Constructor: Initializes a Circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * self.radius ** 2

# Example usage
def main():
    shapes = [
        Rectangle(5, 10),
        Circle(7),
        Rectangle(3, 4),
        Circle(1.5)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is {shape.area():.2f}")

if __name__ == "__main__":
    main()
