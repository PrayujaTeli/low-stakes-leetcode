#currency converter

originalcurrencyname = input("Enter the original currency name: ")
destinationcurrencyname = input("Enter the destination currency name: ")
converstionrate = float(input("Enter the convertion rate: "))
Originalamount = float(input("Enter the original amount: "))
Convertedamount = Originalamount * converstionrate
round(Convertedamount)
print(Convertedamount)