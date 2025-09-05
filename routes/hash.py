from flask import Flask, request, jsonify, Blueprint
from crypto.hash.md2 import md2_hash
from crypto.hash.md5 import md5_hash
from crypto.hash.sha1 import sha1_hash
from crypto.hash.sha224 import sha224_hash
from crypto.hash.sha256 import sha256_hash
from crypto.hash.sha512 import sha512_hash
from crypto.hash.md4 import md4_hash


hash_bp = Blueprint("Hash", __name__)

@hash_bp.route("/md2", methods=["POST"])
def md2_hash_route():
    data = request.get_json()
    text = data.get("text", "")
    hashed = md2_hash(text)
    return jsonify({"Hash": hashed})

@hash_bp.route("/md4", methods=["POST"])
def md4_hash_route():
    data = request.get_json()
    text = data.get("text", "")
    hashed = md4_hash(text)
    return jsonify({"Hash": hashed})
    
@hash_bp.route("/md5", methods=["POST"])
def md5_hash_route():
    data = request.get_json()
    text = data.get("text", "")
    hashed = md5_hash(text)
    return jsonify({"Hash": hashed})
    
@hash_bp.route("/sha1", methods=["POST"])
def sha1_hash_route():
    data = request.get_json()
    text = data.get("text", "")
    hashed = sha1_hash(text)
    return jsonify({"Hash": hashed})

@hash_bp.route("/sha224", methods=["POST"])
def sha224_hash_route():
    data = request.get_json()
    text = data.get("text", "")
    hashed = sha224_hash(text)
    return jsonify({"Hash": hashed})

@hash_bp.route("/sha256", methods=["POST"])
def sha256_hash_route():
    data = request.get_json()
    text = data.get("text", "")
    hashed = sha256_hash(text)
    return jsonify({"Hash": hashed})

@hash_bp.route("/sha512", methods=["POST"])
def sha512_hash_route():
    data = request.get_json()
    text = data.get("text", "")
    hashed = sha512_hash(text)
    return jsonify({"Hash": hashed})

