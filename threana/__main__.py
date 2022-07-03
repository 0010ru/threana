from threana.api.prompt import PromptApi
from threana.api.user_machine import UserMachineApi


def main() -> None:
    print(
        PromptApi().generate(
            user_machine=UserMachineApi().get_user_machine(),
        ),
    )


if __name__ == '__main__':
    main()
