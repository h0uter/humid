from humid import generate


def test_basic():
    my_id = generate()
    assert isinstance(my_id, str)
