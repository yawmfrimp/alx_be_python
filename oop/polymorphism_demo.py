class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError('derived classes need to override this method')
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        if not isinstance(length, (int,float)):
            raise TypeError('Length must be an integer or float')
        if not isinstance(width, (int, float)):
            raise TypeError('Length must be an integer or float')
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        if not isinstance(radius, (int,float)):
            raise TypeError('Length must be an integer or float')
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius)** 2