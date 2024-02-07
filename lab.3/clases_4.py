import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"point coordinates:({self.x},{self.y})")
    def move(self,new_x,new_y):
        self.x=new_x
        self.y=new_y
        print("Point moved to new coordinates")
    def dist(self,other_point):
        distance=math.sqrt((self.x-other_point.x)**2+(self.y-other_point.y))
        return distance
point1=Point(1,2)
point2=Point(4,6)
point1.show()
point1.move(3,5)
point1.show()
distance=point1.dist(point2)
print(f"Distance point1 and point 2:{distance}")
