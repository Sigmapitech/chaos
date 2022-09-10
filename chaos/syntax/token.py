from dataclasses import dataclass
from enum import auto, IntEnum
from typing import Optional


class TokenType(IntEnum):
    INTEGER = auto()
    STRING = auto()

    def __str__(self):
        return self.name


@dataclass
class Token:
    type: TokenType
    value: Optional[str]

    def __repr__(self):
        token_value = f"=>{self.value}" * (self.value is not None)
        return f"<{self.type}{token_value}>"
