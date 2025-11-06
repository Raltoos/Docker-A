from flask import Flask, request, jsonify
from datetime import datetime
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process():
    # accept both JSON and form data
    data = request.get_json(silent=True)
    if not data:
        data = request.form.to_dict()
    name = data.get('name', '')
    email = data.get('email', '')
    message = data.get('message', '')

    # simple processing: return summary
    result = {
        "status": "received",
        "name": name,
        "email": email,
        "message_length": len(message),
        "received_at": datetime.utcnow().isoformat() + "Z"
    }
    return jsonify(result), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Not for production - docker uses gunicorn below; this helps local dev
    # app.run(host="0.0.0.0", port=port, debug=True)
    app.run(host="127.0.0.1", port=5000, debug=True)
    print("Backend running on port", port)

    
