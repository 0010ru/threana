from dataclasses import dataclass

from threana.models.machine import Machine
from threana.models.user import User


@dataclass
class UserMachine:
    user: User
    machine: Machine
