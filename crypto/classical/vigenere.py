#vigenere

def vigenere_Encrypt(text, key):
    result = []
    key = key.upper()
    key_index =0
    for char in text:
        if(char.isalpha()):
            ofc = ord('A') if char.isupper()else ord('a')
            k = ord(key[key_index % len(key)]) - ord('A')
            encrypted = chr((ord(char)-ofc+k)%26 +ofc)
            result.append(encrypted)
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

def vigenere_decrypt(text, key):
    result = []
    key = key.upper()
    key_index =0
    for char in text:
        if(char.isalpha()):
            ofc = ord('A')if char.isupper() else ord('a')
            k = ord(key[key_index % len(key)])- ord ('A')
            decrypted = chr((ord(char)-ofc-k)% 26 + ofc)
            result.append(decrypted)
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

