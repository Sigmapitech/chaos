from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


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

    def __repr__(self) -> str:
        return f"({self.value!r})"


class IntLeaf(Leaf):
    value: int
