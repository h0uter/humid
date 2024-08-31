from humid import helpers
from humid.core import ORDER

# def maximum_chance_of_collision():
#     duplicate_probability = helpers.calc_probability_of_duplicate(ORDER)
#     assert duplicate_probability <


def test_maximum_1_in_XXXXX_chance_of_collision():
    XXXXX = 131_562_000_000  # prob at 30-08-2024
    duplicate_probability = helpers.one_in_XXXXX_chance_of_duplicate(ORDER)
    assert duplicate_probability > XXXXX
