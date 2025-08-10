from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of jokes
jokes = [
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "I only know 25 letters of the alphabet. I don't know y."
]

@app.route('/')
def home():
    return jsonify(message="Welcome to the Random Joke API 🎉")

@app.route('/joke', methods=['GET'])
def get_joke():
    return jsonify(joke=random.choice(jokes))

if __name__ == '__main__':
    app.run(debug=True)

