#! venv/bin/python3
# from main import UserModel
from flask_restful import fields, marshal_with, reqparse, Resource

# Define fields
resource_fields = {
    "userID": fields.Integer,
    "username": fields.String,
    "name": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    "email": fields.String
}


class User(Resource):
    """Handle CRUD operations for users"""

    @marshal_with(resource_fields)
    def get(self, userID):
        result = UserModel.filter_by(userID=userID).first()
        return result

    def put():
        pass

    def patch():
        pass

    def delete():
        pass
