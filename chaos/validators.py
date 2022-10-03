import os
from argparse import ArgumentTypeError


def file_or_directory(arg_path):
    if not os.path.exists(arg_path):
        raise ArgumentTypeError(
            "The specified path does not exist. "
            "Please specify a valid path."
        )

    return arg_path


def lint_rule(_arg_rule):
    return True
