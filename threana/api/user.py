from threana.models.user import User
from threana.repos.user import UserRepo


class UserApi:

    def __init__(self) -> None:
        self._repo = UserRepo()

    def get_user(self) -> User:
        return User(
            name=self._repo.get_username(),
        )
