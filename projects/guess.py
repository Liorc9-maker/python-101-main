import random

num = random.randint(1, 10)
guess = None

count = 7
while count > 0:
    print(f"You have {count} tries")
    count -= 1
    if guess != num:
        guess = int(input("Guess a number between 1 and 10:\n "))
        if guess == num:
            print("Congratulations! \nYou won!")
            break
        else:
            print("nope, sorry. try again!")
