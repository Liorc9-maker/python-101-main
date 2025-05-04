# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4
string_input = input("please type some text to check the first occurense of a letter: \n")
letter_input = input("Which letter would you like to check? \n")
print(f"{string_input},\nLetter to check: {letter_input} \nResult: {string_input.index(letter_input)}")