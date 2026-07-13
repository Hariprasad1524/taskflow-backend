from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

tasks = [
    {"id": 1, "task": "Learn OpenShift Pods", "done": True},
    {"id": 2, "task": "Master Services & Networking", "done": False},
    {"id": 3, "task": "Deploy with Operators", "done": False}
]

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to TaskFlow Backend API!",
        "hostname": socket.gethostname()
    })

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/tasks')
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
