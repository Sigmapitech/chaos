from typing import Optional

from .token import Token, TokenType


class Tokenizer:

    def __init__(self, string):
        self.string = string
        self.__pos = 0

    def next_token(self) -> Optional[Token]:
        if self.eof:
            return None

        if self.cursor.isdigit():
            n = ''
            while not self.eof and self.cursor.isdigit():
                n += self.cursor
                self.__pos += 1

            return Token(TokenType.INTEGER, n)

        if self.cursor == '"':
            s = ''
            self.__pos += 1
            while not self.eof and self.cursor != '"':
                s += self.cursor
                self.__pos += 1

            self.__pos += 1
            return Token(TokenType.STRING, s)

        raise NotImplementedError("Unknown Token", self.cursor)

    @property
    def cursor(self) -> str:
        return self.string[self.__pos]

    @property
    def eof(self) -> bool:
        return self.__pos >= len(self.string)
