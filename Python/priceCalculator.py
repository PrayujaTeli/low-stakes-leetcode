Original_Price = float(input("Please enter product price: "))
Discounted_Fraction = Original_Price * 0.10
Discounted_Price = Original_Price - Discounted_Fraction
Tax_Fraction = Discounted_Price * 0.08
Taxed_Price = Discounted_Price + Tax_Fraction
# round(Taxed_Price, 2)
print("Your final bill is", round(Taxed_Price, 2))