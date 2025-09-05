from Crypto.Hash import SHA224

def sha224_hash(data: str)-> str:
    h = SHA224.new()
    h.update(data.encode('utf-8'))
    return h.hexdigest()
