from entities.user import User
from repositories.user_repository import user_repository as default_user_repository


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(User(username, password))

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")
        alphabet = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        if len(username) < 3:
            raise UserInputError("Username too short")
        if len(password) < 8:
            raise UserInputError("Password too short")
        if password != password_confirmation:
            raise UserInputError("Passwords don't match")
        for c in username:
            if c not in alphabet:
                raise UserInputError("Username contains illegal character")
        if self._user_repository.find_by_username(username) != None:
            raise UserInputError("Username is in use")
        allowed = False
        for c in password:
            if c not in alphabet:
                allowed = True
        if allowed == False:
            raise UserInputError("Invalid password")


user_service = UserService()
