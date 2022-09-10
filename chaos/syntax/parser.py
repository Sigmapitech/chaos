from .token import Token


class Parser:

    def __init__(self, string):
        self.__string = string

    def parse(self):
        return self.integer()

    def integer(self) -> Token:
        return Token(
            type='INTEGER',
            value=int(self.__string),
            raw=self.__string
        )
