"""The command line interface for humid."""

import argparse

from .core import hrid


def main():
    """Runs the cli."""
    parser = argparse.ArgumentParser(description="humid generates human readable ids.")
    parser.add_argument(
        "-n", "--number", type=int, help="The number of hrids to generate.", default=1
    )

    args = parser.parse_args()

    for _ in range(args.number):
        print(hrid())


def print_as_list(strings: list[str]):
    """Print a list of words as string so it can be copy pasted into one of the files in `src/humid/words/`."""
    for element in strings:
        print(f'"{element}",')
