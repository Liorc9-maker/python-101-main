# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.
sarcastic_text = input('Please share your honest opinion with me:\n')
result = ''
upper = True

for char in sarcastic_text:
    if char.isalpha():
        if upper:
            result += char.upper()
        else:
            result += char.lower()
        upper = not upper
    else:
        result += char

print(result)