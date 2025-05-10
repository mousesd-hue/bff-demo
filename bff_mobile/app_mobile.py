from flask import Flask, jsonify, request
from models import User, Session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # permite peticiones desde el frontend (si están en otro puerto)

@app.route('/api/users', methods=['GET'])
def get_users():
    session = Session()
    users = session.query(User).all()
    result = [{"id": u.id, "name": u.name} for u in users]
    session.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)