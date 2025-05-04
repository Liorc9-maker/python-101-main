# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.
num = int(input('Please type in any number between 0 and 1,000,000,000:\n'))
counter = 0
while counter <= num:
    if counter == num:
        print(f"Found the number: {counter}")
        break
    counter += 1