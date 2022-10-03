from abc import abstractmethod
from typing import Callable

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
    ):
        super().__init__(help_)
        self.short = f'-{short}'
        self.name = f'--{name}'

    def is_valid(self, argument: str) -> bool:
        return argument in {self.short, self.name}
