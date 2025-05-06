# TODO: Write a prompt that asks users to "type something to win"
#       They will only win if they type "something" into the prompt
#
# Collect user input
# Compare to the string "something"
# Print a win or lose message
user_input = input("type something to win :")
user_input = user_input.lower()
if user_input == "something":
    print("You won... nothing! :)")
else:
    print("You lost :(")