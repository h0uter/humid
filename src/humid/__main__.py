import argparse

from humid import hrid


def main():
    parser = argparse.ArgumentParser(description="humid generates human readable ids.")
    # parser.add_argument("--foo", type=str, help="A sample argument for foo")
    # parser.add_argument("--bar", type=int, help="A sample argument for bar")

    parser.parse_args()

    print(hrid())
