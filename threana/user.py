from getpass import getuser

from threana.platform import Platform


class User:

    def __init__(self) -> None:
        self.username = getuser()
        self.platform = Platform()
