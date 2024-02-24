import math

def cot(x):
    return 1 / math.tan(x)

def area(s, l):
    return 0.25 * s * l**2 * cot(math.pi / s) 

sides = int(input("Number of sides: "))
length = int(input("Length of a side: "))
print("Area of polygon:", area(sides, length))
