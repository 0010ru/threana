from typing import Literal

from threana.models.system import System
from threana.repos.system.system import SystemRepo


class WinRepo(SystemRepo[Literal[System.WINDOWS]]):
    pass
