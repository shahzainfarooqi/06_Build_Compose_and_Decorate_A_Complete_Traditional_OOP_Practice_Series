from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Abstract method to calculate area"""
        pass



class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print(f"[Rectangle] Created with width={self.width}, height={self.height}")

    def area(self):
        calculated_area = self.width * self.height
        print(f"[Rectangle] Calculated area: {calculated_area}")
        return calculated_area



def main():
  

    print("Creating a Rectangle:")
    rect = Rectangle(5, 10)
    area = rect.area()
    print(f"Area of the rectangle: {area}")


if __name__ == "__main__":
    main()
