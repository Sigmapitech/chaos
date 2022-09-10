import re
from typing import Optional

from .token import Token, TokenType

specs = (
    (re.compile(r'^\s+'), TokenType.WHITESPACE),
    (re.compile(r'^/{2}.*'), TokenType.COMMENT),
    (re.compile(r'^/\*[\s\S]*?\*/'), TokenType.MULTILINE_COMMENT),

    (re.compile(r'^\d+'), TokenType.INTEGER),
    (re.compile(r'^"[^"]*"'), TokenType.STRING),
    (re.compile(r"^'[^']'"), TokenType.CHAR),
)


class Tokenizer:

    def __init__(self, string):
        self.string = string
        self.__pos = 0

    def next_token(self) -> Optional[Token]:
        if self.eof:
            return None

        string = self.string[self.__pos:]

        for pattern, token_type in specs:
            match = re.search(pattern, string)

            if not match:
                continue

            self.__pos += len(token_val := match[0])
            return Token(token_type, token_val)

        raise NotImplementedError(
            f"Unknown Token for {self.string} at pos {self.__pos}"
        )

    @property
    def eof(self) -> bool:
        return self.__pos >= len(self.string)
