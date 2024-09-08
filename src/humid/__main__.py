"""Entrypoint when running humid as module with `python -m humid`."""

import argparse

from humid import hrid


def main():
    """Runs the cli."""
    parser = argparse.ArgumentParser(description="humid generates human readable ids.")
    parser.add_argument(
        "-n", "--number", type=int, help="The number of hrids to generate.", default=1
    )

    args = parser.parse_args()

    for _ in range(args.number):
        print(hrid())


if __name__ == "__main__":
    main()
