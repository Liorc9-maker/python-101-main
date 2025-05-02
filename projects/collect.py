user_input = input("Enter something for Python to echo back: ")
input = " "
for alternating_caps in range(len(user_input)):
    if alternating_caps % 2 == 0:
        input += user_input[alternating_caps].upper()
    else:
        input += user_input[alternating_caps].lower()
print(input)
