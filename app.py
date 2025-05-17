from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        "message": "Hello from our toy Python app!",
        "timestamp": datetime.datetime.now().isoformat(),
        "status": "working"
    })

@app.route('/about')
def about():
    return jsonify({
        "app_name": "Toy Python App",
        "version": "1.0.0",
        "description": "A simple demonstration Flask application"
    })

@app.route('/time')
def current_time():
    return jsonify({
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": "UTC"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)