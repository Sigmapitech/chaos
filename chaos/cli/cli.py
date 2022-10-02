from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .argument import Argument
    from .command import Command
    from typing import Tuple


class CLI:

    def __init__(
        self,
        description: str,
        epilog: str,
        global_args: Tuple[Argument],
        commands: Tuple[Command, ...],
        version: str
    ):
        self.description = description
        self.epilog = epilog
        self.global_args = global_args
        self.version = version

        self.commands = {
            'help': self._help,
            'version': self._version
        }

        self.commands.update(
            {
                command.name: command
                for command in commands
            }
        )

    def parse_args(self, args):
        ...

    def _help(self, *_args):
        print(self.description)
        print(self.epilog)

    def _version(self, *_args):
        print(self.version)
