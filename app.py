
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from routes.classical import classical_bp
from routes.modern import modern_bp
from routes.hash import hash_bp

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_key")

app.register_blueprint(classical_bp, url_prefix="/classical")
app.register_blueprint(modern_bp, url_prefix="/modern")
app.register_blueprint(hash_bp, url_prefix="/hash")

if __name__ =="__main__":
    PORT = int(os.getenv("FLASK_RUN_PORT", 5000))
    DEBUG = os.getenv("FLASK_DEBUG", "False")=="True"
    app.run(host='0.0.0.0', port= PORT, debug=DEBUG)
    
    