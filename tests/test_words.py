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


def test_no_dashses_in_words():
    """Test whether there are undesired dashes in any of the words."""
    all_words = sum(ORDER, [])
    words_with_dashes = []

    for word in all_words:
        if "-" in word:
            words_with_dashes.append(word)

    print(f"{words_with_dashes=}")
    assert len(words_with_dashes) == 0


def test_no_prefixed_usage_of_another_word():
    """Checks if a word is not an existing word with a suffix."""
    all_words = sum(ORDER, [])
    starting_with_other_word: list[tuple[str, str]] = []

    for word in all_words:
        other_words = set(all_words)
        other_words.remove(word)

        for other_word in list(other_words):
            if other_word.startswith(word):
                starting_with_other_word.append((other_word, word))

    print(starting_with_other_word)
    assert len(starting_with_other_word) == 0


def test_no_suffixed_usage_of_another_word():
    """Checks if a word is not an existing word with a suffix."""
    all_words = sum(ORDER, [])
    starting_with_other_word: list[tuple[str, str]] = []

    for word in all_words:
        other_words = set(all_words)
        other_words.remove(word)

        for other_word in list(other_words):
            if other_word.endswith(word):
                starting_with_other_word.append((other_word, word))

    print(starting_with_other_word)
    assert len(starting_with_other_word) == 0


def test_minimum_human_readable_part_length():
    """check whether the minimum length of the human readable part is within bounds"""
    assert False


def test_maximum_human_readable_part_length():
    """check whether the maximum length of the human readable part is within bounds"""
    assert False
