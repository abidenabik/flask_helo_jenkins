from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Hello from Flask + Jenkins + Docker!"})

@main.route('/health')
def health():
    return jsonify({"status": "OK", "service": "flask_hello_jenkins"})
