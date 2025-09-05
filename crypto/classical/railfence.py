

def railFence_encrypt(text, key):
    if key == 1:
        return text

    table = [['' for _ in range(len(text))] for _ in range(key)]

    row = 0
    direction = 1  # 1 -> le bas, -1 ->> le haut

    for col in range(len(text)):
        table[row][col] = text[col]

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    result = ''
    for r in range(key):
        for c in range(len(text)):
            if table[r][c] != '':
                result += table[r][c]

    return result

def railFence_decrypt(text, key):
    if key == 1:
        return text

    table = [['' for _ in range(len(text))] for _ in range(key)]

    row = 0
    direction = 1
    for col in range(len(text)):
        table[row][col] = '*'  
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        row += direction

    index = 0
    for r in range(key):
        for c in range(len(text)):
            if table[r][c] == '*' and index < len(text):
                table[r][c] = text[index]
                index += 1

    result = ''
    row = 0
    direction = 1
    for col in range(len(text)):
        result += table[row][col]
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        row += direction

    return result