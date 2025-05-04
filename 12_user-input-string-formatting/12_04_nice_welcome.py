# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.
name_inp = input("Please type your name:\n")
print(f"Welcome to my script {name_inp.split()[0]}.")