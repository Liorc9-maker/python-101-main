string = "eaeLeteEereNeaeTeieNegeCeaePese"
solution = ""
for index, char in enumerate(string):
    if index % 2 == 1:
        solution += char
print(solution)