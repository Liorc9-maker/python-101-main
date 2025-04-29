# Write a code snippet that gives a name to a `sheep`
# and uses a boolean value to define whether it has `wool` or not.
sheep_name = input("Enter the sheep's name: ")
wool_input = input(("Does the sheep have wool? input (yes/no) ")).lower()
has_wool = wool_input == "yes"
if has_wool is True:
    print(sheep_name," has wool.")
else:
    print(sheep_name," Doesn't have wool")
