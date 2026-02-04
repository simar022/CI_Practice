from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Flask is running CI/CD!")

if __name__ == "__main__":
    # The server only runs if this file is executed directly
    app.run(host='0.0.0.0', port=5000)
