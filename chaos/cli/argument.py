from typing import Callable

ArgPredicate = Callable[[str], bool]


class Argument:

    def __init__(self, help_: str):
        self.help = help_


class NamedArgument(Argument):

    def __init__(self, name: str, help_: str, validation: ArgPredicate):
        super().__init__(help_)
        self.name = name
        self.validation = validation


class ModifierArgument(Argument):

    def __init__(
        self,
        short: str,
        name: str,
        help_: str,
    ):
        super().__init__(help_)
        self.short = short
        self.name = name
