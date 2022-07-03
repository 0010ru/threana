from enum import Enum


class System(Enum):
    WINDOWS = 'Windows'


class Shell(Enum):
    CMD = 'Command Prompt'
    PWSH = 'PowerShell'


class Term(Enum):
    WINCONS = 'Windows Console'
    WINTERM = 'Windows Terminal'
