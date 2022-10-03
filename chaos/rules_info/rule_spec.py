from enum import IntEnum

from pygments import highlight
from pygments.styles import get_style_by_name
from pygments.formatters import TerminalFormatter
from pygments.lexers import CLexer


_lexer = get_style_by_name('dracula')
_formatter = TerminalFormatter(style=_lexer())


class Block:
    def __init__(self, type_, content):
        self.type = type_
        self.content = content

    def __repr__(self):
        return highlight(self.content, CLexer(), _formatter)


class Severity(IntEnum):
    NONE = 0
    INFO = 1
    MINOR = 2
    MAJOR = 3

    def __str__(self):
        return self.name.lower()


class Check(IntEnum):
    NONE = 0
    PARTIAL = 1
    FULL = 2

    def __str__(self):
        return self.name.lower()


class RuleSpec:

    def __init__(
        self,
        title: str,
        description: str,
        severity: str,
        check: str,
        file_type: str
    ):
        self.title = title
        self.description = description

        self.severity = Severity(int(severity))
        self.check = Check(int(check))

        self.file_types = file_type

        self.blocks = self.parse_description()

    def parse_description(self):
        blocks = []

        text = new_block = block_type = ''

        for line in self.description.split('\n'):
            if line.startswith('```') and not block_type:
                block_type = line[3:]
                blocks.append(text)
                text = ''
                continue

            if line == '```':
                blocks.append(Block(block_type, new_block))
                block_type = ''
                continue

            line += '\n'
            if block_type:
                new_block += line
            else:
                text += line

        if text:
            blocks.append(text)
        return blocks

    def __str__(self):
        output = []
        for b in self.blocks:
            output.extend(str(b).split('\n'))

        return (
            f"{self.title} ({self.severity}, {self.check})\n    "
            + '\n     '.join(output)
        )
