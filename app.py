from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of jokes
jokes = [
    "Why did the computer go to the doctor? Because it caught a virus!",
    "Why do Java developers wear glasses? Because they can’t C#!",
    "Why was the math book sad? Because it had too many problems.",
    "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats."
]

@app.route('/')
def home():
    return "<h1>Welcome!</h1><p>Visit /joke for a random joke.</p>"

@app.route('/joke')
def joke():
    return jsonify({"joke": random.choice(jokes)})

@app.route('/health')
def health_check():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

