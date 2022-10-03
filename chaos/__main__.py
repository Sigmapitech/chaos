import os
import sys

from chaos import __version__
from chaos.cli import CLI, Command, ModifierArgument, NamedArgument
from chaos.commands import lint, fix, more

cli = CLI(
    name="chaos",
    version=__version__,
    description='Chaos is a linter for ensuring the Epitech norm',
    epilog='CHAOS: heuristic analyzer of syntax',
    global_args=(
        ModifierArgument(
            short='d',
            name='debug',
            help_="Enable debug mode",
        ),
    ),
    global_command=Command(
        name='lint',
        command=lint,
        args=(
            NamedArgument(
                'path',
                help_='Path to the file to be linted',
                validation=os.path.exists
            ),
        )
    ),
    commands=(
        Command(
            name='fix',
            command=fix,
            args=(
                NamedArgument(
                    'path',
                    help_='Path to the file to be fixed',
                    validation=os.path.exists
                ),
            )
        ),
        Command(
            name='more',
            command=more,
            args=(
                NamedArgument(
                    'rule',
                    help_='Name of the lint rule',
                    validation=lambda: True
                ),
            ),
        )
    )
)


def main():
    command = cli.get_command(*sys.argv[1:])
    command.run()


if __name__ == '__main__':
    main()
