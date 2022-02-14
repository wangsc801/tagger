from flask_login import UserMixin
from database import Base
from sqlalchemy import Column, Integer, String


class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32))
    password = Column(String(32))
    role = Column(Integer)

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
