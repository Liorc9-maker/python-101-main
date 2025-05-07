# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import random

hearts = 7
tries = 0
num = random.randint(0,10)
while tries < hearts:
    tries += 1
    guess = int(input("Guess the number between 0 and 10:\n"))
    if guess == num:
        print("You won!")
        break   
    else:
        print(f"You have {hearts -tries} more tries")
        print("Try again")
if guess != num:
    print("Sorry, you lost. The number was:", num)        