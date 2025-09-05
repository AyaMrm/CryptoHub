from flask import Flask, request, jsonify, Blueprint
from crypto.classical.ceasar import ceasar_encrypt, ceasar_decrypt
from crypto.classical.vigenere import vigenere_Encrypt, vigenere_decrypt
from crypto.classical.playfair import playfair_encrypt, playfair_decrypt
from crypto.classical.railfence import railFence_encrypt, railFence_decrypt

classical_bp = Blueprint("Classical", __name__)

@classical_bp.route('/ceasar/encrypt', methods=["POST"])
def ceasar_encrypt_route():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", 3)
    result = ceasar_encrypt(text, key)
    return jsonify({"ciphertext": result})

@classical_bp.route('/ceasar/decrypt', methods=["POST"])
def ceasar_decrypt_route():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", 3)
    result = ceasar_decrypt(text, key)
    return jsonify({"plaintext": result})


@classical_bp.route('/vigenere/encrypt', methods=["POST"])
def vigenere_encrypt_route():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", 3)
    result = vigenere_Encrypt(text, key)
    return jsonify({"ciphertext": result})

@classical_bp.route('/vigenere/decrypt', methods=["POST"])
def vigenere_decrypt_route():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", 3)
    result = vigenere_decrypt(text, key)
    return jsonify({"plaintext": result})

@classical_bp.route('/playfair/encrypt', methods=["POST"])
def playfair_encrypt_route():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", 3)
    result = playfair_encrypt(text, key)
    return jsonify({"ciphertext": result})

@classical_bp.route('/playfair/decrypt', methods=["POST"])
def playfair_decrypt_route():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", 3)
    result = playfair_decrypt(text, key)
    return jsonify({"plaintext": result})

@classical_bp.route('/railfence/encrypt', methods=["POST"])
def railfence_encrypt_route():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", 3)
    result = railFence_encrypt(text, key)
    return jsonify({"ciphertext": result})

@classical_bp.route('/railfence/decrypt', methods=["POST"])
def railfence_decrypt_route():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", 3)
    result = railFence_decrypt(text, key)
    return jsonify({"plaintext": result})