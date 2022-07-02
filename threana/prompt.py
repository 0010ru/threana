from threana.user import User


class Prompt:

    def generate(self, user: User) -> str:
        return f'[{user.platform.type}:{user.platform.name}:{user.platform.shell}] ({user.username}) > '
