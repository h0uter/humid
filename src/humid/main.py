import random

from humid import helpers

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


def generate() -> str:
    """Returns a human readable identifier."""
    SEP = "-"
    print(
        # f"The probability of intersection = {calc_probability_of_duplicate() * 100:.2e}%"
        f"The probability of intersection is 1 in {"{:,}".format(helpers.calc_1_in_XXXXX_chance_of_duplicate(ORDER)).replace(",", ".")}"
    )

    selection: list[str] = []
    for words_to_choose_from in ORDER:
        selection.append(random.choice(words_to_choose_from))

    the_id = SEP.join(selection)

    return the_id
