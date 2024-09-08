"""The command line interface for humid."""

import argparse

from ._words import W
from .core import hrid


def generate():
    """Runs the cli for generating new hrid's."""
    parser = argparse.ArgumentParser(description="humid generates human readable ids.")
    parser.add_argument(
        "-n", "--number", type=int, help="The number of hrids to generate.", default=1
    )

    args = parser.parse_args()

    for _ in range(args.number):
        print(hrid())


def check_word():
    """Checks new words against existing library."""
    parser = argparse.ArgumentParser(
        description="Check if a word already in the humid dictionary."
    )
    parser.add_argument(
        "-w", "--word", type=str, help="The word to check against the existing library."
    )

    args = parser.parse_args()

    all_words = [word for sublist in W.values() for word in sublist]

    if args.word:
        print(f"Word already in humid dictionary: {args.word in all_words}")


def print_as_list(strings: list[str]):
    """Print a list of words as string so it can be copy pasted into one of the files in `src/humid/words/`."""
    for element in strings:
        print(f'"{element}",')
