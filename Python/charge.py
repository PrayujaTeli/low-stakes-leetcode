import math

def coulombs_law(charge1, charge2, distance):
    F = ((8.9875 * math.pow(10, 9))* charge1 * charge2)/math.pow(distance, 2)
    return F


if __name__ == "__main__":
    charge1 = int(input("charge1: "))
    charge2 = int(input("charge2: "))
    distance = float(input("distance: "))
                     
    result = coulombs_law(charge1, charge2, distance)
    print(result)