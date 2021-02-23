# venv/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import fields, marshal_with, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database/database.db'
db = SQLAlchemy(app)

# Define fields
user_fields = {
    "userID": fields.Integer,
    "username": fields.String,
    "name": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    "email": fields.String
}


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
