from abc import ABC
from typing import Generic, TypeVar

from threana.models.system import Shell, System, Term

TS = TypeVar('TS', bound=System)


class SystemRepo(Generic[TS], ABC):

    def get_shell(self) -> Shell:
        raise NotImplementedError

    def get_term(self) -> Term:
        raise NotImplementedError
