import random
import string

from .words.age import AGES
from .words.animals import ANIMALS
from .words.color import COLORS
from .words.opininion import OPINIONS
from .words.origin import ORIGINS
from .words.pokemon import pokemon_names as NAMES
from .words.shape import SHAPES
from .words.size import SIZES

"""The order in which the hrid is constructed."""
ORDER = [
    OPINIONS + SIZES + AGES + SHAPES + COLORS + ORIGINS,
    NAMES + ANIMALS,
]

"""The separator for the hrid"""
SEP = "-"


def make_identifier(length=22) -> str:
    """Generate a random alphanumeric string.

    Returns:
        str: The random string.
    """
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def hrid() -> str:
    """Returns a default human readable identifier.


    Returns:
        str: The human readable identifier based on elements in `ORDER`.
    """
    selection: list[str] = []
    for words in ORDER:
        selection.append(random.choice(words))

    """Add the identifier string"""
    selection.append(make_identifier())

    the_id = SEP.join(selection)

    return the_id
