from flask import Flask, request, jsonify

#pb des X 
def key_preparation(key):
    key = key.upper().replace("J", "I")
    result = []
    seen = set()
    for char in key:
        if char.isalpha() and char not in seen:
            result.append(char)
            seen.add(char)
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char not in seen :
            result.append(char)
            seen.add(char)
    grid = [result[i*5:(i+1)*5] for i in range(5)]
    return grid

def position(grid, char):
    for row in range(5):
        for col in range(5):
            if grid[row][col]==char:
                return (row, col)
    return None, None

def text_preparation(text):
    text = text.upper().replace("J", "I")
    clean = [c for c in text if c.isalpha()]
    result = []
    i=0
    while i< len(clean):
        a= clean[i]
        if i+1 < len(clean):
            b = clean[i+1]
            if a==b:
                result.append((a, 'X'))
                i+=1
            else:
                result.append((a,b))
                i+=2
        else:
            result.append((a, 'X'))
            i+=1
    return result

def playfair_encrypt(text, key):
    grid = key_preparation(key)
    pairs = text_preparation(text)
    encrypted =[]
    for pair in pairs:
        if len(pair) !=2:
            raise ValueError(f"Invalid pair length: {pair}")
        a, b = pair
        row1, col1 = position(grid, a)
        row2, col2 = position(grid, b)
        
        if row1 == row2:
            encrypted += grid[row1][(col1 + 1) % 5]
            encrypted += grid[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted += grid[(row1 + 1) % 5][col1]
            encrypted += grid[(row2 + 1) % 5][col2]
        else:
            encrypted += grid[row1][col2]
            encrypted += grid[row2][col1]
    return ''.join(encrypted)

def playfair_decrypt(text, key):
    grid = key_preparation(key)
    if len(text) % 2 !=0:
        raise ValueError("Ciphertext length must be even !")
    pairs =[]
    i=0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        pairs.append((a,b))
        i+=2
    decrypted = ""
    for (a, b) in pairs:
        row1, col1 = position(grid, a)
        row2, col2 = position(grid, b)

        if row1 == row2:
            decrypted += grid[row1][(col1 - 1) % 5]
            decrypted += grid[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted += grid[(row1 - 1) % 5][col1]
            decrypted += grid[(row2 - 1) % 5][col2]
        else:
            decrypted += grid[row1][col2]
            decrypted += grid[row2][col1]
    
    for char in decrypted:
        if char == 'X':
            decrypted = decrypted.replace(char, '')
    return decrypted
        