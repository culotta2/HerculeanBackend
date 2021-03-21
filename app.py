from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
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

@app.route('/')
def hello_world():
    return 'hello world'

    
if __name__ == "__main__":
    app.run(debug=True)