import random
from uuid import uuid4

BD_EXAMPLE = "snapshot_fewest-goby-UJDUrIoLN8V2DeCyTv4FkA=="
BD_EXAMPLE_end = "UJDUrIoLN8V2DeCyTv4FkA"


def get_random_part() -> str:
    base_uuid4 = uuid4()

    uuid_suffix = "".join(str(base_uuid4).split("-")[-3:])  # last 3 segments

    print(uuid_suffix)
    print(len(uuid_suffix))

    return uuid_suffix


def random_capitalize(sentence: str) -> str:
    # check performance list vs generator comprehension: https://stackoverflow.com/a/52942594
    return "".join(
        [
            random.choice((str.upper, str.lower))(c) if c.isalpha() else c
            for c in sentence
        ]
    )
