from Crypto.Cipher import DES
from typing import Tuple

BLOCK_SIZE = 8

def pkcs5_pad(data: bytes) -> bytes:
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([pad_len]) * pad_len

def pkcs5_unpad(data: bytes) -> bytes:
    if not data or len(data) % BLOCK_SIZE != 0:
        raise ValueError("Invalid padded data")
    pad_len = data[-1]
    if pad_len < 1 or pad_len > BLOCK_SIZE:
        raise ValueError("Invalid padding length")
    if data[-pad_len:] != bytes([pad_len]) * pad_len:
        raise ValueError("Invalid padding")
    return data[:-pad_len]

def ensure_key(key: bytes) -> bytes:
    if not isinstance(key, (bytes, bytearray)) or len(key) != 8:
        raise ValueError("DES key must be 8 bytes long")
    return key

def des_encrypt(plaintext: str, key: bytes, mode: str = "ECB", iv: bytes | None = None) -> Tuple[bytes, bytes]:
    key = ensure_key(key)
    padded = pkcs5_pad(plaintext.encode("utf-8"))
    if mode.upper() == "CBC":
        if iv is None:
            raise ValueError("IV is required for CBC mode")
        if len(iv) != BLOCK_SIZE:
            raise ValueError("IV has to be 8 bytes long")
        cipher = DES.new(key, DES.MODE_CBC, iv=iv)
        c = cipher.encrypt(padded)
        return iv, c
    elif mode.upper() == "ECB":
        cipher = DES.new(key, DES.MODE_ECB)
        c = cipher.encrypt(padded)
        return b"", c
    else:
        raise ValueError("Mode not supported (only ECB or CBC)")

def des_decrypt(iv: bytes, ciphertext: bytes, key: bytes, mode: str = "CBC") -> bytes:
    key = ensure_key(key)
    if mode.upper() == "CBC":
        if iv is None or len(iv) != BLOCK_SIZE:
            raise ValueError("IV invalid")
        cipher = DES.new(key, DES.MODE_CBC, iv=iv)
        padded = cipher.decrypt(ciphertext)
        return pkcs5_unpad(padded)
    elif mode.upper() == "ECB":
        cipher = DES.new(key, DES.MODE_ECB)
        padded = cipher.decrypt(ciphertext)
        
        return pkcs5_unpad(padded)
    else:
        raise ValueError("Mode not supported (only ECB or CBC)")