import sys

from chaos.__main__ import main as run_chaos


program = """3301"""


def main():
    sys.argv.clear()
    sys.argv.extend(
        (
            "venv/bin/chaos",
            program
        )
    )

    run_chaos()


if __name__ == '__main__':
    main()
