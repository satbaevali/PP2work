import math
sides=int(input("Input number of sides:"))
length=float(input("Input the length of a side:"))
area=(sides*length**2)/(4*math.tan(math.pi/sides))
print(f"The area of the polygon is:",int(area))