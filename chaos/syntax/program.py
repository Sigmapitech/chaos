from dataclasses import dataclass
from typing import List

from .token import Token


@dataclass
class Program:
    body: List[Token]

    def __repr__(self):
        return ', '.join(map(repr, self.body))
