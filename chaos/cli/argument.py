from abc import abstractmethod
from typing import Callable, Optional

ArgPredicate = Callable[[str], bool]


class Argument:

    def __init__(self, help_: str):
        self.help = help_

    @abstractmethod
    def is_valid(self, argument: str) -> bool:
        ...


class NamedArgument(Argument):

    def __init__(self, name: str, help_: str, validation: ArgPredicate):
        super().__init__(help_)
        self.name = name
        self.validation = validation

    def is_valid(self, argument: str) -> bool:
        return self.validation(argument)


class ModifierArgument(Argument):

    def __init__(
        self,
        short: str,
        name: str,
        help_: str,
        command_name: Optional[str] = None,
    ):
        super().__init__(help_)
        self.short = f'-{short}'
        self.name = f'--{name}'

        self.command_name = command_name

    @property
    def is_command(self):
        return self.command_name is not None

    def is_valid(self, argument: str) -> bool:
        return argument in {self.short, self.name}
