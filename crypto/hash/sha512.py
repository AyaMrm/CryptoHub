from Crypto.Hash import SHA512

def sha512_hash(data: str)-> str:
    h = SHA512.new()
    h.update(data.encode('utf-8'))
    return h.hexdigest()
