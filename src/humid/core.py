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

"""
The order in which the hrid is constructed.
"""
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

SEP = "-"


def hrid() -> str:
    """Returns a human readable identifier.


    Returns:
        str: The human readable identifier based on elements in`ORDER`.
    """
    selection: list[str] = []
    for words_to_choose_from in ORDER:
        selection.append(random.choice(words_to_choose_from))

    the_id = SEP.join(selection)

    return the_id


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
