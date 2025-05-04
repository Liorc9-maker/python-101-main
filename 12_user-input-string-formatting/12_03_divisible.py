# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.
number_inp = int(input("Please type in any number between 1 and 1,000,000,000:\n"))
if number_inp % 3 == 0:
    print(f"{number_inp} is divisible by 3.")
else:
    print(f"{number_inp} isn't divisible by 3.")
                 