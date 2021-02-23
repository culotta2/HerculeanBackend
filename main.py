#! venv/bin/python3
from flask import Flask
from flask_restful import Api, fields, marshal_with, Resource
# import hashlib
# import bcrypt
from flask_sqlalchemy import SQLAlchemy

# Init the app
app = Flask(__name__)
api = Api(app)

# Configure the database
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"

db.create_all()

# Define fields
user_fields = {
    "userID": fields.Integer,
    "username": fields.String,
    "name": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    "email": fields.String
}

# Instantiate Model


class UserModel(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    salt = db.Column(db.String(29), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(1), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"User(username = {username}, name = {name})"


class User(Resource):
    """Handle CRUD operations for users"""

    @marshal_with(user_fields)
    def get(self, userID):
        result = UserModel.filter_by(userID=userID).first()
        return result

    def put():
        pass

    def patch():
        pass

    def delete():
        pass


# Add to db
api.add_resource(User, "/User")

admin = User(
    username="dom1127",
    password="1234",
    salt="4321",
    name="Dom",
    age=22,
    sex="M",
    email="nunya@business.net"
)

# Add to the database
db.session.add(admin)
db.session.commit()

# Query the database
print(UserModel.query.all())

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
