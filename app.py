from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 最新の送信データを保存する変数
latest_data = {"value": ""}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_data():
    global latest_data
    data = request.json
    latest_data["value"] = data.get("value", "")
    print("受信:", latest_data["value"])
    return jsonify({"status": "ok"})

@app.route("/get", methods=["GET"])
def get_data():
    return jsonify(latest_data)
