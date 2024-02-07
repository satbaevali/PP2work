class Shape:
    def __init__(self):
        self.area=0
    def sum_area(self):
        print("Area:",self.area)
class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.length=length
        self.sum_area()
    def sum_area(self):
        self.area=self.length**2
        print("Area square:",self.area)
square_a=Square(5)
shape_a=Shape()
shape_a.sum_area()
    