# flask_ngrok_example.py
from flask import Flask
from flask_ngrok import run_with_ngrok

def ngrok():
    app = Flask(__name__)
    run_with_ngrok(app)  # Start ngrok when app is run

    @app.route("/")
    def hello():
        return 