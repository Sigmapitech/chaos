import sys

from chaos.__main__ import main as __run_chaos
from chaos.syntax.ast import IntLeaf, AST, Program, Leaf

programs = [
    '3301',
    '"hello"',
    '"42"'
]


def get_ast_leaf(ast: AST) -> AST:
    assert isinstance(ast, Program)
    return ast.body


def main():
    ast = get_ast_leaf(run_chaos('3301'))
    assert isinstance(ast, IntLeaf)
    assert ast.value == 3301

    ast = get_ast_leaf(run_chaos('"42"'))
    assert isinstance(ast, Leaf)
    assert ast.value == '"42"'

    print(run_chaos('/* Epitech\nNorminette */42  "foo" 69'))


def run_chaos(program) -> AST:
    sys.argv.clear()
    sys.argv.extend(
        (
            "venv/bin/chaos",
            program
        )
    )

    return __run_chaos()


if __name__ == '__main__':
    main()
