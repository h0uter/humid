"""The core of the humid library."""

import random
import string

from ._words import W

ORDER = [
    # first part
    W["opinions"] + W["sizes"] + W["ages"] + W["shapes"] + W["colors"] + W["origins"],
    # second part
    W["pokemons"] + W["animals"],
]
"""The order in which the hrid is constructed."""

SEPARATOR = "-"
"""The separator for the hrid"""

CHARACTERS = string.ascii_letters + string.digits
"""The characters used for generating the identifier"""


def _make_identifier(length: int = 22) -> str:
    """Generate a random alphanumeric string.

    Returns:
        str: The random string.
    """
    return "".join(random.choices(CHARACTERS, k=length))


def hrid() -> str:
    """Returns a default human readable identifier.

    Returns:
        str: The human readable identifier based on elements in `ORDER`.

    Examples:
        >>> hrid()
        'modest-tarpon-oSYCzJPazgTg94KqiEb392'
    """
    selection: list[str] = []
    for words in ORDER:
        selection.append(random.choice(words))

    """Add the identifier string"""
    selection.append(_make_identifier())

    the_id = SEPARATOR.join(selection)

    return the_id
