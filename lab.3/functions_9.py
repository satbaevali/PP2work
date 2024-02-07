import math 
def solve_valume(radius):
    valume=(4/3)*math.pi*radius**3
    return valume
radius=int(input())
print(solve_valume(radius))