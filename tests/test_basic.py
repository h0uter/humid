"""These tests validate the basic workings of the package."""

from humid import hrid


def test_basic():
    """Test whether a hrid is outputted of the correct type."""
    my_id = hrid()
    assert isinstance(my_id, str)
