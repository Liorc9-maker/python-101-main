lowercase_letters ="abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
cipher_text = " "
for char in secret:
    if char.islower():
        index = lowercase_letters.index(char)
        shifted_index = (index + cipher) % 26
        cipher_text += lowercase_letters[shifted_index]
    elif char.isupper():
        lowercase_char = char.lower()
        index = lowercase_letters.index(lowercase_char)
        shifted_index = (index + cipher) % 26
        cipher_text += lowercase_letters[shifted_index].upper()
    else:
        cipher_text += char    


print(cipher_text)    
text = ""
for i, char in enumerate(cipher_text):
    if char.islower():
        
        index = lowercase_letters.index(char)
        shifted_index = (index - cipher) % 26
        text += lowercase_letters[shifted_index]
    elif char.isupper():
        lowercase_char = char.lower()
        index = lowercase_letters.index(lowercase_char)
        shifted_index = (index - cipher +26) % 26
        text += lowercase_letters[shifted_index].upper()
    else:
        text += char
print(text)
