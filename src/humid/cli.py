"""The command line interface for humid."""

import argparse

from ._words import W
from .core import hfid


def generate():
    """Runs the cli for generating new hfid's."""
    parser = argparse.ArgumentParser(description="humid generates human readable ids.")
    parser.add_argument(
        "-n", "--number", type=int, help="The number of hfids to generate.", default=1
    )

    args = parser.parse_args()

    for _ in range(args.number):
        print(hfid())


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


def print_for_copy_paste(strings: list[str]):
    """Print for easy copy pasting into one of the files in `src/humid/words/`."""
    for element in strings:
        print(f'"{element}",')
