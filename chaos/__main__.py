import argparse
import sys

from . import __version__


def main():
    _, *args = sys.argv

    parser = argparse.ArgumentParser(

    )

    parser.add_argument(
        '-d',
        '--debug',
        action='store_true',
        help='Enable debug mode'
    )

    parser.add_argument(
        '-v', '--version',
        action='version', version=f'%(prog)s {__version__}'
    )

    subparsers = parser.add_subparsers(dest='command')
    info = subparsers.add_parser('more', help='Details about a given rule')
    info.add_argument('rule', type=str, help='The rule to inspect')

    fix = subparsers.add_parser('fix', help='Format the code to fix a bunch of rules')
    fix.add_argument('path', type=str, help='Path to the code to format')

    run = subparsers.add_parser('run', help='Run the rule')
    run.add_argument('path', type=str, help='Path to the code to lint')

    parsed_args = parser.parse_args(args)

    print('=>', parsed_args.command)
    print(parsed_args)


if __name__ == '__main__':
    main()
