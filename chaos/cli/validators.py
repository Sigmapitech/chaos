import argparse
import os


def valid_path(arg_path: str, write_access: bool = False) -> str:
    if not os.path.exists(arg_path):
        raise argparse.ArgumentTypeError("file or directory does not exists")

    if not os.access(arg_path, os.R_OK):
        raise argparse.ArgumentTypeError("cannot access file or directory")

    if write_access and not os.access(arg_path, os.W_OK):
        raise argparse.ArgumentTypeError("cannot write to file or directory")

    return arg_path
