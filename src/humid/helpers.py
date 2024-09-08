"""Various helpers."""

from typing_extensions import deprecated

from humid._core import ORDER


@deprecated("new hrids generation no longer matches this calculation")
def _probability_of_duplicate(list_lists_of_words: list[list[str]]):
    lengths = []
    odds = 1
    for list in list_lists_of_words:
        lengths.append(len(list))

    for length in lengths:
        odds *= 1 / length

    return odds


@deprecated("new hrids generation no longer matches this calculation")
def _one_in_XXXXX_chance_of_duplicate(list_lists_of_words: list[list[str]]):
    lengths = []
    odds = 1
    for list in list_lists_of_words:
        lengths.append(len(list))

    for length in lengths:
        odds *= 1 / length

    one_in_x = 1 / odds
    one_in_x_rounded = int(round(one_in_x))

    return one_in_x_rounded


def _show_risk() -> None:
    one_in_xxx = f"{_one_in_XXXXX_chance_of_duplicate(ORDER):,}".replace(",", ".")
    probability_percentage = f"{_probability_of_duplicate(ORDER) * 100:.2e}%"
    print(
        f"Probability of UUID collision is 1 in {one_in_xxx} AKA {probability_percentage}"
    )


def print_as_list(strings: list[str]):
    """Print a list of words as string so it can be copy pasted into one of the files in `src/humid/words/`."""
    for element in strings:
        print(f'"{element}",')
