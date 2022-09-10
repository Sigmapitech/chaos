import sys

from . import __version__


def main():
    print(f'Running Chaos v{__version__}')
    print(sys.argv)


if __name__ == '__main__':
    main()
