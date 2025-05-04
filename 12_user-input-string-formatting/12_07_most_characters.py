# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings
str1 = input("Please type in the first string:\n")
str2 = input("Please type in the second string:\n")
str3 = input("Please type in the third string.:\n")
print(str1) 
print(str2) 
print(str3)
if len(str1) >= len(str2) and len(str1) >= len(str3):
    print(len(str1), str1)
if len(str2) >= len(str1) and len(str2) >= len(str3):
    print(len(str2), str2)
if len(str3) >= len(str1) and len(str3) >= len(str2):
    print(len(str3), str3)    