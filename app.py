import re
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine
from mongoengine import NotUniqueError


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
    def validate_cpf(self, cpf):
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            return False

        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validação do primeiro dígito verificador:
        sum_of_products = sum(
            a*b for a, b in zip(numbers[0:9], range(10, 1, -1))
        )
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True

    def post(self):
        data = _user_parser.parse_args()

        if not self.validate_cpf(data["cpf"]):
            return {"message": "CPF is invalid!"}, 300

        try:
            response = UserModel(**data).save()
            return {
                "message": f"User {response.first_name} {response.last_name} successfully created!"
            }, 201
        except NotUniqueError:
            return {
                "message": "CPF already exists in database!"
            }, 400

    def get(self, cpf):
        return {"message": f"user and {cpf}"}


api.add_resource(Home, '/')
api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
