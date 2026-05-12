"""
Sankar Group – Hindi + Telugu Voice Bot Backend
Run:  pip install flask flask-cors
      python server.py
Then: ngrok http 5000
"""

from flask import Flask, send_file, jsonify, request
from flask_cors import CORS
import json, os, datetime

app = Flask(__name__)
CORS(app)

LOG_FILE = "conversation_logs.json"

def load_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_log(role, text):
    logs = load_logs()
    logs.append({
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "role": role,
        "text": text
    })
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)

@app.route("/")
def index():
    return send_file("voicebot.html")

@app.route("/api/log", methods=["POST"])
def log_message():
    data = request.json
    save_log(data.get("role", "user"), data.get("text", ""))
    return jsonify({"status": "ok"})

@app.route("/api/logs", methods=["GET"])
def get_logs():
    return jsonify(load_logs())

@app.route("/api/logs/clear", methods=["DELETE"])
def clear_logs():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    return jsonify({"status": "cleared"})

if __name__ == "__main__":
    print("=" * 50)
    print("  Sankar Group Voice Bot – Starting server...")
    print("  Open: http://localhost:5000")
    print("  For public URL: ngrok http 5000")
    print("=" * 50)
    app.run(debug=True, port=5000)
