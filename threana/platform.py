from platform import node, system


class Platform:

    def __init__(self) -> None:
        self.name = node()
        self.type = system()
        self.shell = self._get_shell()

    def _get_shell(self) -> str:
        pass
