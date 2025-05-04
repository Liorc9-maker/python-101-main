# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.
investment_amount = float(input("Please type in the investment amount:\n"))
interest_rate = float(input("Please type in the investment rate:\n"))
num_of_years = int(input("Please type in the numbers of years that you would like to invest:\n"))
value = investment_amount * (1 + (interest_rate/100))**num_of_years
print(f"The futur value of your investment is: {value}")