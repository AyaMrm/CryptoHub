from Crypto.Hash import MD5

def md5_hash(data: str)-> str:
    h = MD5.new()
    h.update(data.encode('utf-8'))
    return h.hexdigest()

