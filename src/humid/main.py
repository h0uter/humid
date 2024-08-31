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


def show_risk() -> None:
    one_in_xxx = "{:,}".format(helpers.one_in_XXXXX_chance_of_duplicate(ORDER)).replace(
        ",", "."
    )
    probability_percentage = f"{helpers.probability_of_duplicate(ORDER) * 100:.2e}%"
    print(
        f"Probability of UUID collision is 1 in {one_in_xxx} AKA {probability_percentage}"
    )


def generate(print_risk=False) -> str:
    """Returns a human readable identifier."""
    if print_risk:
        show_risk()

    SEP = "-"
    selection: list[str] = []
    for words_to_choose_from in ORDER:
        selection.append(random.choice(words_to_choose_from))

    the_id = SEP.join(selection)

    return the_id
