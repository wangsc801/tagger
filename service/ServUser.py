from model.User import User


class ServUser:
    def __init__(self, user: User):
        self.user = user

    def is_inputed_password_correct(self, password: str) -> bool:
        if password != self.user.password:
            return False
        return True

    def get_by_id(id: int) -> User:
        return User.query.get(id)

    def get_by_username(username: str) -> User:
        return User.query.filter_by(username=username).first()
