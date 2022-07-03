from platform import uname

from threana.models.machine import Machine
from threana.models.system import Shell, System, Term


class MachineApi:

    def get_machine(self) -> Machine:
        # TODO: get value from repo
        system_info = uname()
        return Machine(
            name=system_info.node,
            system=System(system_info.system),
            shell=Shell.PWSH,  # noqa: S604
            term=Term.WINTERM,
        )
