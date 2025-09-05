from Crypto.Hash import MD4

def md4_hash(data:str)->str:
    h = MD4.new()
    h.update(data.encode('utf-8'))
    return h.hexdigest()
