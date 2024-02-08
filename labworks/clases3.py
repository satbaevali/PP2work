class myshape():
    def __init__(self,color="black",is_filled=True):
        self.color=color
        self.is_filled=is_filled
    def __str__(self):
        return f"Myshape -Color:{self.color},Is_filled:{self.is_filled}"
    def getarea(self):
        return 0
class Restangle(myshape):
    def __init__(self,color,is_filled,x_top_left, y_top_left, length, width):
        super().__init__(color,is_filled)
        self.x_top_left=x_top_left
        self.y_top_left=y_top_left
        self.length=length
        self.width=width
    def getarea(self):
        return self.length*self.width
    def __str__(self):
        return (
            f"Rectangle - Color: {self.color}, Is Filled: {self.is_filled}, "
            f"X: {self.x_top_left}, Y: {self.y_top_left}, Length: {self.length}, Width: {self.width}, "
            f"Area: {self.getarea()}"
        )
class circle(myshape):
    def __init__(self,color,is_filled,x_center,y_center,radius):
        super().__init__(color,is_filled)
        self.x_center=x_center
        self.y_center=y_center
        self.radius=radius
    def getarean(self):
        return 3,14*self.radius**2
    def __str__(self):
        return (
            f"Circle - Color: {self.color}, Is Filled: {self.is_filled}, "
            f"X: {self.x_center}, Y: {self.y_center}, Radius: {self.radius}, "
            f"Area: {self.getarean()}"
        )
color_input = input("Enter color for Rectangle: ")
is_filled_input = input("Is Rectangle filled? (True/False): ").capitalize()  # Convert input to boolean
x_top_left_input = float(input("Enter X coordinate for top-left corner: "))
y_top_left_input = float(input("Enter Y coordinate for top-left corner: "))
length_input = float(input("Enter length of Rectangle: "))
width_input = float(input("Enter width of Rectangle: "))
rectangle_shape = Restangle(
    color=color_input,
    is_filled=is_filled_input,
    x_top_left=x_top_left_input,
    y_top_left=y_top_left_input,
    length=length_input,
    width=width_input
)

color_input= input("Enter color for Circle: ")
is_filled_input = input("Is Circle filled? (True/False): ").capitalize() 
x_center_input=float(input("Enter x on center: "))
y_center_input=float(input("Enter y on center: "))
radius_input=float(input("Enter radius: "))
circle_shape=circle(
    color=color_input,
    is_filled=is_filled_input,
    x_center=x_center_input,
    y_center=x_center_input,
    radius=radius_input
    
)

#print(rectangle_shape)
print(circle_shape)