from .ages import AGES
from .animals import ANIMALS
from .colors import COLORS
from .materials import MATERIALS
from .opinions import OPINIONS
from .origins import ORIGINS
from .pokemons import POKEMONS
from .purposes import PURPOSES
from .quantities import QUANTITIES
from .shapes import SHAPES
from .sizes import SIZES

W: dict[str, list[str]] = {
    # adjectives
    "ages": AGES,
    "colors": COLORS,
    "opinions": OPINIONS,
    "origins": ORIGINS,
    "shapes": SHAPES,
    "sizes": SIZES,
    "quantities": QUANTITIES,
    "materials": MATERIALS,
    "purposes": PURPOSES,
    # Nouns
    "animals": ANIMALS,
    "pokemons": POKEMONS,
}
"""All the words that are available for generation of hfid's"""

__all__ = ["W"]
