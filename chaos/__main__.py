import sys

from .syntax.parser import Parser
from . import __version__


def main():
    print(f'Running Chaos v{__version__}')
    if len(sys.argv) < 2:
        print("Please provide a program as string.")
        return

    print(sys.argv[1])
    parser = Parser(sys.argv[1])
    print("Parsing AST...")
    return parser.parse()


if __name__ == '__main__':
    print(main())
