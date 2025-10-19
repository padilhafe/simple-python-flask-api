import pytest
from application import create_app
from config.mock import MockConfig


class TestApplication():

    @pytest.fixture()
    def client(self):
        app = create_app(MockConfig)
        return app.test_client()

    @pytest.fixture()
    def valid_user(self):
        return {
            "first_name": "First",
            "last_name": "Surname",
            "cpf": "057.065.580-35",
            "email": "first.surname@hotmail.com",
            "birth_date": "01-11-1966"
        }

    @pytest.fixture()
    def invalid_user(self):
        return {
            "first_name": "First",
            "last_name": "Surname",
            "cpf": "057.065.580-34",
            "email": "first.surname@hotmail.com",
            "birth_date": "01-11-1966"
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 201
        assert b"successfully created" in response.data

        response = client.post('/user', json=invalid_user)
        assert response.status_code == 400
        assert b"CPF is invalid!" in response.data

        response = client.post('/user', json=valid_user)
        assert response.status_code == 400
        assert b"CPF already exists in database!" in response.data

    def test_get_user(self, client, valid_user, invalid_user):
        response = client.get(f'/user/{valid_user["cpf"]}')
        assert response.status_code == 200
        assert response.json["first_name"] == valid_user["first_name"]
        assert response.json["last_name"] == valid_user["last_name"]
        assert response.json["cpf"] == valid_user["cpf"]
        assert response.json["email"] == valid_user["email"]
        assert response.json["birth_date"] == valid_user["birth_date"]

        response = client.get(f'/user/{invalid_user["cpf"]}')
        assert response.status_code == 400
        assert b"User does not exist in database." in response.data
