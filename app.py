from flask import Flask, jsonify
import random

app = Flask(__name__)

# Sample list of jokes
jokes = [
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "I told my computer I needed a break, and it said: 'No problem — I'll go to sleep.'",
    "Why was the math book sad? It had too many problems.",
    "I only know 25 letters of the alphabet. I don't know y.",
    "Why do cows wear bells? Because their horns don't work."
]

@app.route('/joke', methods=['GET'])
def get_joke():
    joke = random.choice(jokes)  # Pick a random joke
    return jsonify({"joke": joke})

if __name__ == '__main__':
    app.run(debug=True)
