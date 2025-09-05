#Ceasar 

def ceasar_encrypt (text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char)-ord('A')+key)%26 + ord('A'))
        elif(char.islower()):
            result += chr((ord(char)-ord('a')+key)%26 + ord('a'))
        else:
            result += char
    return result

def ceasar_decrypt(text, key):
    return ceasar_encrypt(text, -key)

