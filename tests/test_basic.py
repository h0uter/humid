from humid import generate


def test_basic():
    my_id = generate()
    assert isinstance(my_id, str)


def test_no_duplicate_id():
    TIMES_TO_GENERATE = 1_000
    ids = set()

    for i in range(TIMES_TO_GENERATE):
        the_id = generate()

        if the_id in ids:
            raise ValueError(f"iter {i}: {the_id} already present in set")

        ids.add(the_id)
