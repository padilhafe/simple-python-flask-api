from .db import db


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True, max_length=50)
    last_name = db.StringField(required=True, max_length=50)
    email = db.EmailField(required=True)
    birth_date = db.DateTimeField(required=True)

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "cpf": self.cpf,
            "email": self.email,
            "birth_date": self.birth_date.strftime("%d-%m-%Y"),
        }
