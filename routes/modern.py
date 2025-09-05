from flask import Flask, request, jsonify, Blueprint
from crypto.modern.aes import aes_encrypt_ECB, aes_decrypt_ECB, aes_encrypt_CBC, decrypt_AES_CBC
from crypto.modern.rc4 import rc4
from crypto.modern.des import des_decrypt_text, des_encrypt_text
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
    else:  # ECB
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
    cipher = des_encrypt_text(text, key)
    return jsonify({"ciphertext": cipher})

@modern_bp.route('/des/decrypt', methods=['POST'])
def des_decrypt_route():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", "").encode()
    cipher = des_encrypt_text(text, key)
    return jsonify({"ptext": cipher})