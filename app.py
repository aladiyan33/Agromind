# AgroMind AI Flask Backend (Render-Ready)
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "AgroMind AI Backend Running ✅",
        "message": "Connected to Render successfully!"
    })

# Example endpoint
@app.route('/chat', methods=['POST'])
def chat_ai():
    data = request.json
    user_msg = data.get('message', '')
    return jsonify({"reply": f"AI says: {user_msg[::-1]}"})  # test echo

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)# Placeholder Flask app - full code to be added here
