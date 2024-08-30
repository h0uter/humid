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

ORDER = [
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


def generate() -> str:
    """Returns a human readable identifier."""
    SEP = "-"

    selection: list[str] = []
    for words_to_choose_from in ORDER:
        selection.append(random.choice(words_to_choose_from))

    the_id = SEP.join(selection)

    return the_id
