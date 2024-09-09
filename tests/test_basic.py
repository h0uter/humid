"""These tests validate the basic workings of the package."""

from humid import hfid


def test_basic():
    """Test whether a hfid is outputted of the correct type."""
    my_id = hfid()
    assert isinstance(my_id, str)
