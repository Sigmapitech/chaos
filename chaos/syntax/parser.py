from typing import List

from .token import Token
from .tokeniser import Tokenizer


class Parser:

    def __init__(self, string):
        self.__string = string
        self.tokenizer = Tokenizer(self.__string)

    def parse(self) -> List[Token]:
        return [self.tokenizer.next_token()]
