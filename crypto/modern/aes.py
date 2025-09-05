from Crypto.Cipher import AES 
import base64

def aes_encrypt_ECB(plaitext: str, key: bytes)-> bytes:
    if len(key) not in {16, 24, 32}:
        raise ValueError("Key must be either 16, 24 or 32 bytes")
    
    cipher = AES.new(key, AES.MODE_ECB)
    plaitext_bytes = plaitext.encode('utf-8')
    padding_length = AES.block_size - (len(plaitext_bytes) % AES.block_size)
    padded_data = plaitext_bytes + (padding_length * chr(padding_length)).encode('utf-8')
    ciphertext = cipher.encrypt(padded_data)
    return base64.b64encode(ciphertext)

def aes_decrypt_ECB(text: str, key: bytes)->str:
    if len(key) not in {16, 24, 32}:
        raise ValueError("Key must be either 16, 24 or 32 bytes")
    
    cipher = AES.new(key, AES.MODE_ECB)
    text = base64.b64decode(text)
    decrypted_bytes = cipher.decrypt(text)
    padding_length = decrypted_bytes[-1]
    return decrypted_bytes[:-padding_length].decode('utf-8')

def aes_encrypt_CBC(text:str, key:bytes)->tuple[bytes, bytes]:
    if len(key) not in {16, 24, 32}:
        raise ValueError("Key must be either 16, 24 or 32 bytes")
    
    cipher = AES.new(key, AES.MODE_CBC)
    text_bytes = text.encode('utf-8')
    padding_length = AES.block_size - (len(text_bytes) % AES.block_size)
    padded_data = text_bytes + (padding_length * chr(padding_length)).encode('utf-8')
    ciphertext = cipher.encrypt(padded_data)
    return cipher.iv, base64.b64encode(ciphertext)

def decrypt_AES_CBC(iv: bytes, ciphertext: str, key: bytes) -> str:
    if len(key) not in [16, 24, 32]:
        raise ValueError("Key must be either 16, 24 or 32 bytes")
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = base64.b64decode(ciphertext)
    decrypted_bytes = cipher.decrypt(ciphertext)
    padding_length = decrypted_bytes[-1]
    return decrypted_bytes[:-padding_length].decode('utf-8')


'''
plaintext = "Hello AES CBC Test!"

    # Clés valides
key_128 = b"1234567890abcdef"                     # 16 bytes
key_192 = b"1234567890abcdef12345678"             # 24 bytes
key_256 = b"1234567890abcdef1234567890abcdef"     # 32 bytes

print("=== Mode ECB ===")
encrypted_ecb = aes_encrypt_ECB(plaintext, key_256)
print("Ciphertext (ECB):", encrypted_ecb)

decrypted_ecb = aes_decrypt_ECB(encrypted_ecb, key_256)
print("Plaintext (ECB):", decrypted_ecb)

print("\n=== Mode CBC ===")
iv, encrypted_cbc = aes_encrypt_CBC(plaintext, key_256)
print("IV (base64):", base64.b64encode(iv).decode())
print("Ciphertext (CBC):", encrypted_cbc)

decrypted_cbc = decrypt_AES_CBC(iv, encrypted_cbc, key_256)
print("Plaintext (CBC):", decrypted_cbc)
'''