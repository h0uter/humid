import random
import string
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


def random_seq() -> str:
    """Generate a random alphanumeric string.

    Returns:
        str: The random string.
    """
    return "".join(random.choices(string.ascii_letters + string.digits, k=22))


cool = get_random_part()

print(cool)

wow = random_capitalize(cool)
print(wow)


print(random_seq())
