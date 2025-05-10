from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simulamos base de datos con una lista
fake_users = []
next_id = 1

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(fake_users)

@app.route('/api/users', methods=['POST'])
def add_user():
    global next_id
    data = request.get_json()
    user = {"id": next_id, "name": data['name']}
    fake_users.append(user)
    next_id += 1
    return jsonify(user), 201

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global fake_users
    fake_users = [u for u in fake_users if u['id'] != user_id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
