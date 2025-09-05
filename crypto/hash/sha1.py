from Crypto.Hash import SHA1

def sha1_hash(data: str)-> str:
    h = SHA1.new()
    h.update(data.encode('utf-8'))
    return h.hexdigest()

