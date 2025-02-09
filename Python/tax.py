HourlyWage = float(input("Enter the hourly wage: "))
Noofhoursperweek = int(input("Enter the Noofhours: "))
weeksperyear = int(input("Enter the weeksperyear: "))
per_week = Total = HourlyWage * Noofhoursperweek
Total = (HourlyWage * Noofhoursperweek) * weeksperyear

print("per week: ", per_week)

print("per year: ", Total)
#This person would make 15.50 ∗ 40 = 620.00 per week.


SSN = Total * 0.06
print(SSN)
NewTotal = Total - SSN
Medicare = NewTotal * 0.02
print(Medicare)
PostMedicare = NewTotal - Medicare
IRS = PostMedicare * 0.12
print(IRS)
postIRS = PostMedicare - IRS
PA = postIRS * 0.0307
print("PA: ", PA)
postPA = postIRS - PA
phila = postPA * 0.0375
print("phila: ", phila)
postphila = postPA - phila
print("postphila: ", postphila)

healthinsurance = postphila - 4752
print("hii: ", healthinsurance)

Newtotalvalue = healthinsurance/weeksperyear
print("hi: ", Newtotalvalue)
Newtotalvalue1 = Newtotalvalue/Noofhoursperweek
#print("hi: ", Newtotalvalue)
