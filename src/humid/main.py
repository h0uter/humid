import random

from .words.age import AGES
from .words.color import COLORS
from .words.material import MATERIALS
from .words.opininion import OPINIONS
from .words.origin import ORIGINS
from .words.pokemon import pokemon_names as NAMES
from .words.purpose import PURPOSES
from .words.quantity import QUANTITIES
from .words.shape import SHAPES
from .words.size import SIZES

save_imports_from_ruff = [
    QUANTITIES,
    OPINIONS,
    SIZES,
    AGES,
    SHAPES,
    COLORS,
    ORIGINS,
    MATERIALS,
    PURPOSES,
    NAMES,
]
ORDER = [
    # QUANTITIES,
    OPINIONS,
    SIZES,
    AGES,
    SHAPES,
    COLORS,
    # ORIGINS,
    # MATERIALS,  # material doesnt make sense for pokemon
    # PURPOSES,
    NAMES,
]


def calc_probability_of_duplicate():
    lengths = []
    odds = 1
    for list in ORDER:
        lengths.append(len(list))

    for length in lengths:
        odds *= 1 / length

    return odds


def calc_1_in_XXXXX_chance_of_duplicate():
    lengths = []
    odds = 1
    for list in ORDER:
        lengths.append(len(list))

    for length in lengths:
        odds *= 1 / length

    one_in_x = 1 / odds
    one_in_x_rounded = int(round(one_in_x))

    return one_in_x_rounded


def generate() -> str:
    """Returns a human readable identifier."""
    SEP = "-"
    print(
        # f"The probability of intersection = {calc_probability_of_duplicate() * 100:.2e}%"
        f"The probability of intersection is 1 in {"{:,}".format(calc_1_in_XXXXX_chance_of_duplicate()).replace(",", ".")}"
    )

    selection: list[str] = []
    for words_to_choose_from in ORDER:
        selection.append(random.choice(words_to_choose_from))

    the_id = SEP.join(selection)

    return the_id
