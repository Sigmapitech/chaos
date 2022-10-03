from __future__ import annotations

from .command import InternalCommand

from functools import partial, wraps
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .argument import Argument
    from .command import Command
    from typing import Tuple


class CLI:

    def __init__(
        self,
        name: str,
        description: str,
        epilog: str,
        global_args: Tuple[Argument],
        commands: Tuple[Command, ...],
        version: str
    ):
        self.name = name
        self.description = description
        self.epilog = epilog
        self.global_args = global_args
        self.version = version

        _help = wraps(self._help)(partial(self._help, self))
        _version = wraps(self._version)(partial(self._version, self))

        self._commands = {
            'help': InternalCommand(command=_help),
            'version': InternalCommand(command=_version)
        }

        self._commands.update(
            {
                command.name: command
                for command in commands
            }
        )

    def _cmd_from_args(self, *args) -> Optional[Command]:
        return None

    def get_command(self, *args) -> Command:
        cmd = self._cmd_from_args(*args)
        return cmd or self._commands['help']

    def _help(self, *_args):
        print(self.description)
        print(self.epilog)

    def _version(self, *_args):
        print(self.version)
