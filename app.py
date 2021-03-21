from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init database
db = SQLAlchemy(app)
# Init marshmallow
ma = Marshmallow(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True)
    name = db.Column(db.String(40))
    email = db.Column(db.String(20))
    phone = db.Column(db.String(15))

    def __init__(self, username, name, email, phone):
        self.username = username
        self.name = name
        self.email = email
        self.phone = phone

# User schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'name', 'email', 'phone')

# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/user', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

@app.route('/user', methods=['POST'])
def add_user():
    username = request.json['username']
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']

    new_user = User(username, name, email, phone)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)

    username = request.json['username']
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']

    user.username = username
    user.name = name
    user.email = email
    user.phone = phone

    db.session.commit()

    return user_schema.jsonify(user)

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()


    
if __name__ == "__main__":
    app.run(debug=True)