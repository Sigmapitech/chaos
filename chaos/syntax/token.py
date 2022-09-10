from dataclasses import dataclass
from typing import Any


@dataclass
class Token:
    type: str
    value: Any
    raw: str

    def __repr__(self):
        token_value = f"={self.value}" * (self.value is not None)
        return f"<[{self.type}{token_value}]>"
