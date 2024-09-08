from .age import AGES
from .animals import ANIMALS
from .colors import COLORS
from .opininions import OPINIONS
from .origin import ORIGINS
from .pokemon import POKEMONS
from .shape import SHAPES
from .size import SIZES

W: dict[str, list[str]] = {
    # adjectives
    "ages": AGES,
    "colors": COLORS,
    "opinions": OPINIONS,
    "origins": ORIGINS,
    "shapes": SHAPES,
    "sizes": SIZES,
    # Nouns
    "animals": ANIMALS,
    "pokemons": POKEMONS,
}
"""All the words that are available for generation of hrid's"""

__all__ = ["W"]
