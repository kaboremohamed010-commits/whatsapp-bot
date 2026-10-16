from flask import Flask, request
import os

app = Flask(__name__)

VERIFY_TOKEN = "devsynapse123"

@app.route("/")
def home():
    return "Bot WhatsApp en ligne !"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        if token == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Token invalide", 403
    data = request.get_json()
    print(data)
    return "OK", 200
