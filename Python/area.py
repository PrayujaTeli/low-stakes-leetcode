import math

dia = int(input("Enter user input: "))
radius = dia/2

areaofcircle = math.pi * math.pow(radius, 2)
areaofsquare= math.pow(dia, 2)
areaoftraingle = (math.sqrt(3)/4) * areaofsquare

print("A circle of diameter", dia, "has an area of", areaofcircle)
print("An equilateral triangle of size", dia, "has an area of", areaoftraingle)
print("A square of size", dia, "has an area of", areaofsquare)