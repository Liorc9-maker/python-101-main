lowercase_letters ="abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
cipher_text = " "
for char in secret.lower():
    if char in lowercase_letters:
        index = lowercase_letters.index(char)
        shifted_index = (index + cipher) % 26
        cipher_text += lowercase_letters[shifted_index]
    elif secret.isalpha(): 
        cipher_text += " "
    else:
        cipher_text += char    


print(cipher_text)    
