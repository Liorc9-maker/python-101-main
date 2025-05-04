# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.
vowels_for_counting = input("Please type in some text:\n").lower()
vowerls = "aeiou"
print(f"""In the text there is a total of {vowels_for_counting.count('a')} of the letter A.
    A total of {vowels_for_counting.count('e')} of the letter E.
    A total of {vowels_for_counting.count('i')} of the letter I.
    A total of {vowels_for_counting.count('o')} of the letter O.
    And a total of {vowels_for_counting.count('u')} of the letter U. """)