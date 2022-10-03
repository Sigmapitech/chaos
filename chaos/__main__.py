import argparse
import sys

from chaos import __version__
from chaos.validators import file_or_directory, lint_rule
from chaos.commands import lint_command, fix_command, more_command

parser = argparse.ArgumentParser(
    description='Chaos is a linter for ensuring the Epitech norm',
    epilog='CHAOS: heuristic analyzer of syntax',
)

parser.add_argument(
    '-v', '--version',
    action='version', version=f'%(prog)s {__version__}'
)

subparsers = parser.add_subparsers(dest='command')

subparsers.add_parser(
    'more',
    help='Details about a given rule'
).add_argument(
    'rule',
    type=lint_rule,
    help='The rule to inspect'
)

subparsers.add_parser(
    'fix',
    help='Format the code to fix a bunch of rules'
).add_argument(
    'path',
    type=file_or_directory,
    help='Path to the code to format'
)

subparsers.add_parser(
    'lint',
    help='Run the rule'
).add_argument(
    'path',
    type=file_or_directory,
    help='Path to the code to lint'
)


def main():
    parsed_args = parser.parse_args(sys.argv[1:])

    if parsed_args.command == 'lint':
        lint_command(parsed_args.path)

    elif parsed_args.command == 'fix':
        fix_command(parsed_args.path)

    else:
        more_command(parsed_args.rule)


if __name__ == '__main__':
    main()
