# Use the built-in `sys` module to explicitly quit your script.
import sys
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
while True:
    user_input = input("Please type something (type 'quit' to exit):\n ")
# If the user enters the word "quit", you can exit the program
    if user_input.lower() == 'quit':
        
# using a functionality provided by this module.
         sys.exit("Exiting the program.")