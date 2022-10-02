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
        ...
