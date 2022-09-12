from .ast import IntLeaf, Program, AST, Leaf
from .token import Token, TokenType
from .tokenizer import Tokenizer


class Parser:

    def __init__(self, string):
        self.__string = string
        self.tokenizer = Tokenizer(self.__string)

        self._look_ahead = self.tokenizer.next_token()

    def parse(self) -> AST:
        foo = []
        while self._look_ahead:
            foo.append(self.literal())

        return Program(foo)

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

        return IntLeaf(value=int(token.value))

    def string(self) -> AST:
        token = self.__eat(TokenType.STRING)
        return Leaf(value=token.value)

    def char(self) -> AST:
        token = self.__eat(TokenType.CHAR)
        return Leaf(value=token.value)

    def whitespace(self):
        token = self.__eat(TokenType.WHITESPACE)
        return Leaf(value=token.value)

    def comment(self):
        token = self.__eat(TokenType.COMMENT)
        return Leaf(value=token.value)

    def multiline_comment(self):
        token = self.__eat(TokenType.MULTILINE_COMMENT)
        return Leaf(value=token.value)

    def literal(self):
        if self._look_ahead.type == TokenType.INTEGER:
            return self.integer()

        elif self._look_ahead.type == TokenType.STRING:
            return self.string()

        elif self._look_ahead.type == TokenType.CHAR:
            return self.string()

        elif self._look_ahead.type == TokenType.WHITESPACE:
            return self.whitespace()

        elif self._look_ahead.type == TokenType.COMMENT:
            return self.comment()

        elif self._look_ahead.type == TokenType.MULTILINE_COMMENT:
            return self.multiline_comment()
