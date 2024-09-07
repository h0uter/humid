from collections import Counter

from humid.core import ORDER


def test_no_duplicates():
    """Test whether there are any duplicates per category."""

    for list_of_words in ORDER:
        duplicates = [
            item for item, count in Counter(list_of_words).items() if count > 1
        ]
        print(f"{duplicates=}")
        assert len(list_of_words) == len(set(list_of_words))


def test_no_duplicates_between():
    """Test whether there are any duplicates in total."""
    all_words = sum(ORDER, [])
    duplicates = [item for item, count in Counter(all_words).items() if count > 1]
    print(f"{duplicates=}")
    assert len(all_words) == len(set(all_words))


def test_no_spaces_in_words():
    """Test whether there are undesired spaces in any of the words."""
    all_words = sum(ORDER, [])
    words_with_spaces = []

    for word in all_words:
        if " " in word:
            words_with_spaces.append(word)

    print(f"{words_with_spaces=}")
    assert len(words_with_spaces) == 0


test_no_spaces_in_words()
