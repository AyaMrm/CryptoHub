from Crypto.Hash import SHA256

def sha256_hash(data: str)-> str:
    h = SHA256.new()
    h.update(data.encode('utf-8'))
    return h.hexdigest()

