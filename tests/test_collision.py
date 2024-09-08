"""These tests validate probability of generating colliding hrids."""

from humid import hrid


def test_no_duplicate_id():
    """Test whether no collisions are encountered when generating N times."""
    TIMES_TO_GENERATE = 1_000_000
    ids = set()

    for i in range(TIMES_TO_GENERATE):
        the_id = hrid()

        if the_id in ids:
            raise ValueError(f"iter {i}: {the_id} already present in set")

        ids.add(the_id)
