from threana.api.machine import MachineApi
from threana.api.user import UserApi
from threana.models.user_machine import UserMachine


class UserMachineApi:

    def __init__(self) -> None:
        self._user_api = UserApi()
        self._machhine_api = MachineApi()

    def get_user_machine(self) -> UserMachine:
        return UserMachine(
            user=self._user_api.get_user(),
            machine=self._machhine_api.get_machine(),
        )
