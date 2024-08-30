from humid import human_id


def test_basic():
    my_id = human_id()
    assert isinstance(my_id, str)
