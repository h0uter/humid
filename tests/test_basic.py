from humid import hrid


def test_basic():
    my_id = hrid()
    assert isinstance(my_id, str)


def test_no_duplicate_id():
    TIMES_TO_GENERATE = 1_000
    ids = set()

    for i in range(TIMES_TO_GENERATE):
        the_id = hrid()

        if the_id in ids:
            raise ValueError(f"iter {i}: {the_id} already present in set")

        ids.add(the_id)
