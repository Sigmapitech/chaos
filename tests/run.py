import sys


programs = [
    '3301',
    '"hello"'
]


def main():
    for program in programs:
        run_chaos(program)


def run_chaos(program):
    sys.argv.clear()
    sys.argv.extend(
        (
            "venv/bin/chaos",
            program
        )
    )

    chaos_mod = __import__('chaos.__main__', fromlist='main')
    chaos_mod.main()
    del chaos_mod


if __name__ == '__main__':
    main()
