from typing import Optional

from .token import Token, TokenType


class Tokenizer:

    def __init__(self, string):
        self.string = string
        self.__pos = 0

    def next_token(self) -> Optional[Token]:
        if self.ended:
            return None

        if self.cursor.isdigit():
            n = ''
            while not self.ended and self.cursor.isdigit():
                n += self.cursor
                self.__pos += 1

            return Token(
                TokenType.INTEGER,
                int(n),
                n
            )

    @property
    def cursor(self) -> str:
        return self.string[self.__pos]

    @property
    def ended(self) -> bool:
        return self.__pos >= len(self.string)
