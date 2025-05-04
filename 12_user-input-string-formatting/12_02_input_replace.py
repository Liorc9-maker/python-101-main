# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please
user_input_text = input("Please type some text:\n")
user_symbol = input("Please type in any symbol:\n")
replace_letter = user_input_text[0]
replace_symbol = user_symbol[0]
new_text = user_input_text.replace(replace_letter, replace_symbol)
print(new_text)