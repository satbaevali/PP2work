import time
import math

def calculate_square(number,ms):
    time.sleep(ms / 1000)  
    result = math.sqrt(number)
    return result
number = float(input("Enter a number: "))
ms = int(input("Enter delay in milliseconds: "))
result = calculate_square(number,ms)
print(f"Square root of {number} after {ms} milliseconds is {result}")

