from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Health check endpoint for liveness probe
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Health check endpoint for readiness probe
@app.route('/ready', methods=['GET'])
def ready_check():
    return jsonify({"status": "ready"}), 200

# Simulated in-memory notification storage
notifications = []

@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.get_json()
    new_notification = {
        "id": len(notifications) + 1,
        "user_id": data['user_id'],
        "message": data['message'],
        "status": "Sent"
    }
    notifications.append(new_notification)
    return jsonify({"message": "Notification sent successfully", "notification": new_notification}), 201

@app.route('/notifications', methods=['GET'])
def get_notifications():
    return jsonify(notifications)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)

