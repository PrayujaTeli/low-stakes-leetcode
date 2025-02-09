import math

costperterm = 19431
totalterms = 12 * costperterm
FR = 0.00458333
Years = 10
months = 12 * Years
A1 = math.pow(1+  0.00458333, months)
A2 = 0.00458333  * A1
A3 = totalterms * (A2/(A1 -1))

#A = totalterms * (FR * math.pow(1 + FR, months)) / (math.pow(1 + FR, months) - 1)

print(totalterms, months, A3)