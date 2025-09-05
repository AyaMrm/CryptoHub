import math
import random

# --- Test primalité ---
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# --- Génération de nombres premiers ---
def generate_prime(minV, maxV):
    prime = random.randint(minV, maxV)
    while not is_prime(prime):
        prime = random.randint(minV, maxV)
    return prime 

# --- Algorithme d'Euclide étendu ---
def gcd(a, b):
    if a == 0:
        return b, 0, 1
    pgcd, x1, y1 = gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return pgcd, x, y

# --- Inverse modulaire ---
def mod_inverse(e, phi):
    pgcd, x, _ = gcd(e, phi)
    if pgcd != 1:
        raise ValueError("Modular inverse does not exist")
    return (x % phi + phi) % phi 

# --- Génération de clés RSA ---
def generate_keypair():
    p = generate_prime(100, 1000)
    q = generate_prime(100, 1000)
    while p == q:
        q = generate_prime(100, 1000)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  
    while math.gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)  # clé publique, clé privée

# --- Chiffrement ---
def rsaENC(public_key, plaintext: str) -> int:
    e, n = public_key
    plaintext_bytes = plaintext.encode("utf-8")
    plaintext_int = int.from_bytes(plaintext_bytes, byteorder="big")
    cipher = pow(plaintext_int, e, n)
    return cipher

# --- Déchiffrement ---
def rsaDEC(private_key, ciphertext: int) -> str:
    d, n = private_key
    plaintext_int = pow(ciphertext, d, n)
    plaintext_length = (plaintext_int.bit_length() + 7) // 8
    plaintext_bytes = plaintext_int.to_bytes(plaintext_length, byteorder="big")
    return plaintext_bytes.decode("utf-8")

# --- Test ---
if __name__ == "__main__":
    public_key, private_key = generate_keypair()
    print("Clé publique:", public_key)
    print("Clé privée:", private_key)

    message = "Hello RSA avec CryptoHub"
    print("\nMessage original:", message)

    cipher = rsaENC(public_key, message)
    print("Chiffré:", cipher)

    plain = rsaDEC(private_key, cipher)
    print("Déchiffré:", plain)
