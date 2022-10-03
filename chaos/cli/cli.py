from __future__ import annotations

from .argument import ModifierArgument
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
        global_command: Command,
        commands: Tuple[Command, ...],
        version: str
    ):
        self.name = name
        self.description = description
        self.epilog = epilog
        self.global_command = global_command
        self.global_args = (
            ModifierArgument(
                short='h',
                name='help',
                help_='Show the help for this command',
                command_name='help'
            ),
            ModifierArgument(
                short='v',
                name='version',
                help_='Show the version of the cli',
                command_name='version'
            )
        ) + global_args
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

    def _check_builtin_args(self, arg):
        for mod in self.global_args:
            if not mod.is_command:
                continue

            if mod.is_valid(arg):
                return self._commands.get(mod.command_name)

    def _cmd_from_args(self, *args) -> Optional[Command]:
        if not args:
            return None

        first_arg = args[0]
        if first_arg.startswith('-'):
            return self._check_builtin_args(first_arg)

        cmd = self._commands.get(first_arg)
        if cmd is not None:
            return cmd

        non_mods = [a for a in args if not a.startswith('-')]
        g_non_mods = [
            a for a in self.global_command.args
            if not isinstance(a, ModifierArgument)
        ]

        return self.global_command if len(non_mods) == len(g_non_mods) else None

    def get_command(self, *args) -> Command:
        cmd = self._cmd_from_args(*args)
        return self._commands['help'] if cmd is None else cmd

    def _help(self, *_args):
        print(self.description)
        print(self.epilog)

    def _version(self, *_args):
        print(self.version)
