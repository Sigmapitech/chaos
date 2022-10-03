from __future__ import annotations
from typing import Callable, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from chaos.cli import Argument


class Command:
    def __init__(
        self,
        name: str,
        command: Callable[[...], None],
        args: Tuple[Argument, ...],
        namespace: bool = True,
    ):
        self.name = name
        self.command = command
        self.args = args
        self.namespace = namespace

    def run(self):
        print(f'running command {self.name}')


class InternalCommand(Command):

    def __init__(
        self,
        command: Callable[[...], None],
    ):
        super().__init__(
            name=command.__name__,
            command=command,
            args=(),
            namespace=True,
        )
