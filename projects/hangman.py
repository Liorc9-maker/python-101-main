# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it

# Hard-coded word to guess
import random
words_list = ["pathlib", "random", "github", "syntaxerror", "python", "git init"]
word_to_guess = random.choice(words_list)
word_display = [' ' if char == ' ' else '_' for char in word_to_guess]
guessed_letters = set()
attempts_remaining = 6

# Game introduction
print("Welcome to Hangman!")
print("Try to guess the word, one letter at a time.")
print(f"You have {attempts_remaining} attempts.")
print(" ".join(word_display))

# Game loop
while attempts_remaining > 0 and '_' in word_display:
    guess = input("Enter a letter: ").lower()

    # Validate input without using string module
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical character.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter. Try a different one.")
        continue

    guessed_letters.add(guess)

    if guess in word_to_guess:
        print(f"Good job! '{guess}' is in the word.")
        for idx, char in enumerate(word_to_guess):
            if char == guess:
                word_display[idx] = guess
    else:
        attempts_remaining -= 1
        print(f"Sorry, '{guess}' is not in the word. Attempts left: {attempts_remaining}")

    print("Current word: " + " ".join(word_display))

# End of game messages
if '_' not in word_display:
    print(f"Congratulations! You guessed the word: '{word_to_guess}'")
else:
    print(f"Game over! The word was: '{word_to_guess}'")
