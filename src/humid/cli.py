"""The command line interface for humid."""


def print_as_list(strings: list[str]):
    """Print a list of words as string so it can be copy pasted into one of the files in `src/humid/words/`."""
    for element in strings:
        print(f'"{element}",')
