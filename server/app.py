from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample data storage (in production, use a database)
submissions = []

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'Flask Backend',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/submit', methods=['POST'])
def handle_form_submission():
    try:
        # Get form data
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Process the data
        submission = {
            'id': len(submissions) + 1,
            'timestamp': datetime.now().isoformat(),
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone', ''),
            'subject': data.get('subject'),
            'message': data.get('message'),
            'processed': True
        }
        
        # Store submission
        submissions.append(submission)
        
        # Return success response
        return jsonify({
            'message': 'Form submitted successfully!',
            'submission_id': submission['id'],
            'processed_data': {
                'name_length': len(submission['name']),
                'email_domain': submission['email'].split('@')[1] if '@' in submission['email'] else '',
                'message_word_count': len(submission['message'].split()),
                'timestamp': submission['timestamp']
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/submissions', methods=['GET'])
def get_submissions():
    return jsonify({
        'total_submissions': len(submissions),
        'submissions': submissions
    })

@app.route('/api/submissions/<int:submission_id>', methods=['GET'])
def get_submission(submission_id):
    submission = next((s for s in submissions if s['id'] == submission_id), None)
    if submission:
        return jsonify(submission)
    else:
        return jsonify({'error': 'Submission not found'}), 404

if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port, debug=True)