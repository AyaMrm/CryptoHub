import base64

def ksa(key: bytes):
    """Key Scheduling Algorithm"""
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    return s

def prga(s: list, length: int):
    """Pseudo-Random Generation Algorithm"""
    i = j = 0
    result = []
    s = s.copy()  # éviter de modifier l'original
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        result.append(s[(s[i] + s[j]) % 256])
    return result

def rc4(data: bytes, key: bytes) -> bytes:
    """RC4 encryption/decryption (symétrique)"""
    s = ksa(key)
    key_stream = prga(s, len(data))
    return bytes([data[i] ^ key_stream[i] for i in range(len(data))])

# Exemple d’utilisation
"""
message = b"Hello RC4!"
key = b"mysetkey"

ciphertext = rc4(message, key)
print("Chiffré (base64) :", base64.b64encode(ciphertext).decode())

decrypted = rc4(ciphertext, key)
print("Déchiffré :", decrypted.decode())
"""
