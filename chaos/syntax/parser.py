from .ast import IntLeaf, Program, AST
from .token import Token, TokenType
from .tokenizer import Tokenizer


class Parser:

    def __init__(self, string):
        self.__string = string
        self.tokenizer = Tokenizer(self.__string)

        self._look_ahead = self.tokenizer.next_token()

    def parse(self) -> AST:
        return Program(self.integer())

    def __eat(self, token_type: TokenType) -> Token:
        token = self._look_ahead

        if token is None:
            raise EOFError(
                f'Unexpected End of string while trying to eat {token_type}'
            )

        if token.type != token_type:
            raise SyntaxError(
                f'Unexpected Token {token}'
                f' while trying to eat {token_type}'
            )

        self._look_ahead = self.tokenizer.next_token()
        return token

    def integer(self) -> AST:
        token = self.__eat(TokenType.INTEGER)
        assert isinstance(token.value, str)

        return IntLeaf(
            value=int(token.value),
            raw_token=token
        )
