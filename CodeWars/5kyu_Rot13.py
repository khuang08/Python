import string

def rot13(message):
    new_message = []
    new_letter = ''

    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)

    for letter in message:

        if letter.islower():
            if letter in alphabet_lower:
                i = alphabet_lower.index(letter)
                if i + 13 >= 26:
                    new_letter = alphabet_lower[(i + 13 - 26)]
                    new_message.append(new_letter)
                else:
                    new_letter = alphabet_lower[i + 13]
                    new_message.append(new_letter)
        elif letter.isupper():
            if letter in alphabet_upper:
                i = alphabet_upper.index(letter)
                if i + 13 >= 26:
                    new_letter = alphabet_upper[(i + 13 - 26)]
                    new_message.append(new_letter)
                else:
                    new_letter = alphabet_upper[i + 13]
                    new_message.append(new_letter)
        else:
            new_message.append(letter)
        
        print(new_letter)

    new_message = str(''.join(new_message))
    return(new_message)

print(rot13("test")) #"grfg"
print(rot13("Test")) #"Grfg"
print(rot13("Pbqrjnef")) #Codewars
