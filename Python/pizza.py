import math
print("Welcome to Mario and Luigi's Pizzeria","\n")
dia = int(input("Enter the diameter of the pizzas you want to order (in inches): "))
noofpeople = int(input("Enter the number of people in your party: "))

area = math.pi* math.pow(dia/2, 2)
slicesperpizza = area/14.125
slicesperpizza = math.floor(slicesperpizza)

total_slices_needed = noofpeople * 3
pizzas_needed = math.ceil(total_slices_needed / slicesperpizza)


print("For a party of", noofpeople, "people you need to order" , pizzas_needed, "pizza(s).")
print("A" , dia, "inch pizza will yield", total_slices_needed,  "slices.")
    



