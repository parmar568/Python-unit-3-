class Shape:
    def area(self):
        return 0  # Default area for a generic shape


class Square(Shape):
    def __init__(self, length):
        self.length = length  # Initialize the length of the square

    def area(self):
        return self.length ** 2  # Calculate the area of the square


# Example usage
if __name__ == "__main__":
    # Create an instance of Shape
    shape = Shape()
    print(f"Area of the shape: {shape.area()}")  # Output: 0

    # Create an instance of Square with a length of 4
    square = Square(4)
    print(f"Area of the square: {square.area()}")  # Output: 16
