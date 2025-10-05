from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 最新データを保持する変数
latest_data = {"value": ""}

# Webページ
@app.route("/")
def index():
    return render_template("index.html")

# データ受信
@app.route("/send", methods=["POST"])
def send():
    global latest_data
    data = request.json
    latest_data["value"] = data.get("value", "")
    print("受信:", latest_data["value"])
    return jsonify({"status": "ok"})

# データ取得
@app.route("/get", methods=["GET"])
def get_data():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
