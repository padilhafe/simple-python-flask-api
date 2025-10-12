from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine


app = Flask(__name__)
api = Api(app)


app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'mongo',
    'port': 27017,
    'username': 'admin',
    'password': 'admin'
}
db = MongoEngine(app)


_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    'first_name',
    type=str,
    required=True,
    help="This field cannot be blank."
)
_user_parser.add_argument(
    'last_name',
    type=str,
    required=True,
    help="This field cannot be blank."
)
_user_parser.add_argument(
    'cpf',
    type=str,
    required=True,
    help="This field cannot be blank."
)
_user_parser.add_argument(
    'email',
    type=str,
    required=True,
    help="This field cannot be blank."
)
_user_parser.add_argument(
    'birth_date',
    type=str,
    required=True,
    help="This field cannot be blank."
)


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True, max_length=50)
    last_name = db.StringField(required=True, max_length=50)
    email = db.EmailField(required=True)
    birth_date = db.DateTimeField(required=True)


class Home(Resource):
    def get(self):
        return {"path": "home"}


class Users(Resource):
    def get(self):
        return {"message": "User 1"}


class User(Resource):
    def post(self):
        data = _user_parser.parse_args()
        UserModel(**data).save()
        return data

    def get(self, cpf):
        return {"message": f"user and {cpf}"}


api.add_resource(Home, '/')
api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
