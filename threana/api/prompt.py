from threana.models.user_machine import UserMachine


class PromptApi:

    def generate(self, user_machine: UserMachine) -> str:
        return '[{system}:{node}:{shell}] ({username}) > '.format(
            system=user_machine.machine.system.value,
            node=user_machine.machine.name,
            shell=user_machine.machine.shell.value,  # noqa: S604
            username=user_machine.user.name,
        )
