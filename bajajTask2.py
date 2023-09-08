from flask import Flask, request, jsonify

app = Flask(__name__)

# Your user information
user_info = {
    "full_name": "Debanjan Basak",
    "dob": "23102001",
    "email": "db6016@srmist.edu.in",
    "roll_number": "RA2011003010606",
}

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'POST':
        data = request.json.get('data', [])

        numbers = [item for item in data if isinstance(item, int) or item.isdigit()]
        alphabets = [item for item in data if isinstance(item, str) and len(item) == 1 and item.isalpha()]

        highest_alphabet = max(alphabets, key=lambda x: x.lower()) if alphabets else []

        response_data = {
            "is_success": True,
            "user_id": f"{user_info['full_name']}_{user_info['dob']}",
            "email": user_info['email'],
            "roll_number": user_info['roll_number'],
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet]
        }
        
        return jsonify(response_data), 200  # HTTP Status Code: 200

    elif request.method == 'GET':
        # Handle GET requests as specified
        response_data = {
            "operation_code": 1
        }
        return jsonify(response_data), 200  # HTTP Status Code: 200

if __name__ == '__main__':
    app.run(debug=True)
