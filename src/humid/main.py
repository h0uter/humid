import random

WORDS = [
    "cool",
    "cat",
    "broke",
]


def human_id() -> str:
    """Returns a human readable identifier."""
    SEP = "-"
    my_id = (
        random.choice(WORDS) + SEP + random.choice(WORDS) + SEP + random.choice(WORDS)
    )
    return my_id
