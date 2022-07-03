from dataclasses import dataclass

from threana.models.system import Shell, System, Term


@dataclass
class Machine:
    name: str
    system: System
    shell: Shell
    term: Term
