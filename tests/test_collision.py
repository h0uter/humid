"""These tests validate probability of generating colliding hrids."""

from humid import helpers
from humid._core import ORDER


def test_maximum_1_in_XXXXX_chance_of_collision():
    """Deprecated."""
    XXXXX = 131_562_000_000  # prob at 30-08-2024
    duplicate_probability = helpers._one_in_XXXXX_chance_of_duplicate(ORDER)
    assert duplicate_probability > XXXXX
