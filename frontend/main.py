from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_URL = "http://localhost:8000/chat/"  # Replace with your api server URL or ngrok URL

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    try:
        response = requests.post(API_URL, json={"message": user_message})
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return jsonify({"error": "Could not reach chatbot API"}), 500

    bot_reply = response.json().get("response", "")
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
