class Shape:
    def __init__(self):
        self.area=0
    def sum_area(self):
        print("Area shape:",self.area)
class Rectangle:
    def __init__(self,length,width):
        super().__init__()
        self.length=length
        self.width=width
        self.sum_area()
    def sum_area(self):
        self.area=self.length*self.width
        print("Area Rectange:",self.area)
length=int(input())
widht=int(input())        
restangle_instance=Rectangle(length, widht)