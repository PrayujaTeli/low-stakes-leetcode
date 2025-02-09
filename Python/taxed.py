import math

def tax(income):
    if income < 11600:
        taxes = income * 0.10
    elif income >= 11601 and income <= 47150:
        taxes = 11600 * 0.10
        taxes += (income - 11600)* 0.12
    elif income >= 47151 and income <= 100525:
        taxes = 11600 * 0.10
        taxes += (47151 - 11600)* 0.12
        taxes += (income - 47151)* 0.24
    return taxes
       

#if __name__ == "__main__":
income = int(input("Income: "))
finaltax = tax(income)
print(finaltax)