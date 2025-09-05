from Crypto.Hash import MD2

def md2_hash(data:str)->str:
    h = MD2.new()
    h.update(data.encode('utf-8'))
    return h.hexdigest()
