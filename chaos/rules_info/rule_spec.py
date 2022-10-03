from enum import IntEnum


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

    def __str__(self):
        return (
            f"{self.title} ({self.severity}, {self.check})\n    "
            + '\n     '.join(self.description.split('\n'))
        )
