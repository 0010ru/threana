from getpass import getuser


class UserRepo:

    def get_username(self) -> str:
        return getuser()
