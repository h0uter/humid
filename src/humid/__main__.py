import argparse

from humid import hrid


def main():
    parser = argparse.ArgumentParser(description="humid generates human readable ids.")
    parser.add_argument(
        "-n", "--number", type=int, help="The number of hrids to generate."
    )

    args = parser.parse_args()

    for _ in range(args.number):
        print(hrid())
