#- Kilometers to drive
# Liters-per-kilometer usage of the car 
# Price per liter of fuel
kilometers = float(input("Please type in how many Kilometers \nyou are planning to drive:\n"))
lit_per_km = float(input("Please type in the \nliters per kilometers usage of your car:\n"))
price_per_lit = float(input("Please type in the price of fuel per liter:\n"))
total = kilometers * lit_per_km * price_per_lit 
print(f"Youre trip will cost a total of {total:.2f} currency units.")