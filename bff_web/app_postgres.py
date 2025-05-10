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

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get("name")
    if not name:
        return {"error": "Nombre requerido"}, 400

    session = Session()
    new_user = User(name=name)
    session.add(new_user)
    session.commit()
    session.close()
    return {"message": "Usuario agregado"}, 201

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    session = Session()
    user = session.get(User, user_id)
    if not user:
        session.close()
        return {"error": "Usuario no encontrado"}, 404

    session.delete(user)
    session.commit()
    session.close()
    return {"message": "Usuario eliminado"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)