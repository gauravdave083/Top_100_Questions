# Abstraction hides the complex implementation details and shows only the essential features of an object.
# In the abstraction example, the Shape class defines the interface but does not implement it, while the Rectangle class provides the specific implementation.


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Usage
rect = Rectangle(10, 5)
print(f"Area: {rect.area()}")         # Outputs: Area: 50
print(f"Perimeter: {rect.perimeter()}") # Outputs: Perimeter: 30