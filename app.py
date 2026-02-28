from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Azure Monitor Dashboard Started 🚀"

@app.route('/api/health')
def health():
    return jsonify({
        "status": "running",
        "message": "API is healthy"
    })

if __name__ == '__main__':
    app.run(debug=True)