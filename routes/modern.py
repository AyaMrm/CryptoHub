from flask import Flask, request, jsonify, Blueprint
from crypto.modern.aes import aes_encrypt_ECB, aes_decrypt_ECB, aes_encrypt_CBC, decrypt_AES_CBC
from crypto.modern.rc4 import rc4
from crypto.modern.des import des_encrypt, des_decrypt
from crypto.modern.rsa import generate_keys, rsa_encrypt, rsa_decrypt
import base64


modern_bp = Blueprint("Modern", __name__)

@modern_bp.route('/aes/encrypt', methods=['POST'])
def aes_encrypt_route():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", "").encode()
    mode = data.get("mode", "ECB").upper()

    if mode == "CBC":
        iv, ciphertext = aes_encrypt_CBC(text, key)
        return jsonify({
            "iv": base64.b64encode(iv).decode(), 
            "ciphertext": base64.b64encode(ciphertext).decode()  
        })
    else:  #ecb
        ciphertext = aes_encrypt_ECB(text, key)
        return jsonify({
            "ciphertext": base64.b64encode(ciphertext).decode()
        })


@modern_bp.route('/aes/decrypt', methods=['POST'])
def aes_decrypt_route():
    data = request.get_json()
    ciphertext_b64 = data.get("text", "")
    key = data.get("key", "").encode()
    mode = data.get("mode", "ECB").upper()

    ciphertext = base64.b64decode(ciphertext_b64)

    if mode == "CBC":
        iv_b64 = data.get("iv", "")
        iv = base64.b64decode(iv_b64)
        text = decrypt_AES_CBC(iv, ciphertext, key)
        return jsonify({"text": text})
    else:  # ECB
        text = aes_decrypt_ECB(ciphertext, key)
        return jsonify({"text": text})

@modern_bp.route('/rc4/encrypt', methods=['POST'])
def rc4_encrypt_toute():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", "")
    text_bytes = text.encode()
    key_bytes = key.encode()
    cipher = rc4(text_bytes, key_bytes)
    return jsonify("ciphertext:", base64.b64encode(cipher).decode())

@modern_bp.route('/rc4/decrypt', methods=['POST'])
def rc4_decrypt_route():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", "")
    key_bytes = key.encode()
    cipher_bytes = base64.b64decode(text)
    plain = rc4(cipher_bytes, key_bytes)
    plaintext = plain.decode(errors="ignore")
    return jsonify({"plaintext": plaintext})

@modern_bp.route('/des/encrypt', methods=['POST'])
def des_encrypt_route():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", "").encode()
    mode = data.get("mode", "ECB").upper()
    iv = data.get("iv", None)
    if iv:
        iv = bytes.fromhex(iv)  
    iv_bytes, ct = des_encrypt(text, key, mode, iv)
    return jsonify({
        "ciphertext": ct.hex(),
        "iv": iv_bytes.hex() if iv_bytes else None
    })

@modern_bp.route('/des/decrypt', methods=['POST'])
def des_decrypt_route():
    data = request.get_json()
    ciphertext = bytes.fromhex(data.get("text", ""))
    key = data.get("key", "").encode()
    mode = data.get("mode", "ECB").upper()
    iv = data.get("iv", None)
    if iv:
        iv = bytes.fromhex(iv)
    pt = des_decrypt(iv, ciphertext, key, mode)
    return jsonify({
        "plaintext": pt.decode("utf-8")
    })

@modern_bp.route('/rsa/encrypt', methods=['POST'])
def rsa_encrypt_route():
    try:
        data = request.get_json()
        text = data.get("text")
        bits = data.get("bits", 1024)
        n = data.get("n")
        p = data.get("p")
        q = data.get("q")
        e = data.get("e")
        
        if not text :
            return jsonify({"error": "Text Field is required ! "})
        
        pub, priv = generate_keys(n=n, p=p, q=q, e=e, bits=bits)
        ciphertext = rsa_encrypt(text, pub)
        return jsonify({
            "public_key": {"n": pub[0], "e": pub[1]},
            "private_key": {"n": priv[0], "d": priv[1]},
            "ciphertext": ciphertext
        })
    except Exception as ex:
        return jsonify({"error": str(ex)}), 400
    

@modern_bp.route('/rsa/decrypt', methods=['POST'])
def rsa_decrypt_route():
    try:
        data = request.get_json(force=True)
        blocks = data.get("blocks")
        priv = data.get("priv")
        p = data.get("p")
        q = data.get("q")
        e = data.get("e")

        if not blocks:
            return jsonify({"error": "Le champ 'blocks' est requis."}), 400

        if priv:
            priv_tuple = (priv["n"], priv["d"])
        else:
            priv_tuple = None

        plaintext = rsa_decrypt(
            blocks,
            priv=priv_tuple,
            p=p,
            q=q,
            e=e
        )

        return jsonify({
            "plaintext": plaintext
        })

    except Exception as ex:
        return jsonify({"error": str(ex)}), 400