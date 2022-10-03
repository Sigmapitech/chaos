import os
from argparse import ArgumentTypeError
from .rules_info import ruleset


def file_or_directory(arg_path):
    if not os.path.exists(arg_path):
        raise ArgumentTypeError(
            "The specified path does not exist. "
            "Please specify a valid path."
        )

    return arg_path


def lint_rule(arg_rule):
    if arg_rule not in ruleset:
        raise ArgumentTypeError(
            "The specified rule does not exist. "
            "Please specify a valid rule."
        )

    return arg_rule
