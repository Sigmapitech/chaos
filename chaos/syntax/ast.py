from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol

from .token import Token


class AST(Protocol):

    def __repr__(self) -> str:
        ...


@dataclass
class Program(AST):
    body: AST

    def __repr__(self) -> str:
        return repr(self.body)


@dataclass
class Leaf(AST):
    value: Any
    raw_token: Token

    def __repr__(self) -> str:
        return f"({self.value}, {self.raw_token})"


class IntLeaf(Leaf):
    value: int
