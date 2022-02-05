from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))
    role = db.Column(db.Integer)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_authenticated(self):
        return super().is_authenticated

    def is_active(self):
        return super().is_active

    def is_anonymous(self):
        return super().is_anonymous

    def get_id(self):
        return super().get_id()

    # def to_string(self):
    #    print(f">> USER:\nusername:{self.username}\npassword:{self.password}")
