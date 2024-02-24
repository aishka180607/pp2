def area_of_trapezoid(x, y, z):
    return (y + z) * x / 2


height = float(input("Height: "))
first_val = float(input("Base, first value: "))
second_val = float(input("Base, second value: "))
print("area of trapezoid:", area_of_trapezoid(height, first_val, second_val))
