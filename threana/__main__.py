from threana.prompt import Prompt
from threana.user import User


def main():
    user = User()
    print(Prompt().generate(user))


if __name__ == '__main__':
    main()
