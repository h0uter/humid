"""These tests validate the words that are used for hrid generation."""

from collections import Counter

import pytest

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
    all_words = [item for sublist in ORDER for item in sublist]
    duplicates = [item for item, count in Counter(all_words).items() if count > 1]
    print(f"{duplicates=}")
    assert len(all_words) == len(set(all_words))


def test_no_spaces_in_words():
    """Test whether there are undesired spaces in any of the words."""
    all_words = [item for sublist in ORDER for item in sublist]
    words_with_spaces = []

    for word in all_words:
        if " " in word:
            words_with_spaces.append(word)

    print(f"{words_with_spaces=}")
    assert len(words_with_spaces) == 0


def test_no_dashses_in_words():
    """Test whether there are undesired dashes in any of the words."""
    all_words = [item for sublist in ORDER for item in sublist]
    words_with_dashes = []

    for word in all_words:
        if "-" in word:
            words_with_dashes.append(word)

    print(f"{words_with_dashes=}")
    assert len(words_with_dashes) == 0


WHITELIST = {"amberjack", "newt", "goldenretriever", "greatdane", "badger"}


def test_later_word_does_not_start_with_earlier_word():
    """Checks if a word is not an existing word with a suffix.But only checks this for words that can follow eachother in the hrid based on their order.

    Example:
        avoid `black-blackbird`
    """
    starting_with_other_word: list[tuple[str, str]] = []

    for i in range(len(ORDER) + 1):
        if i == len(ORDER) - 1:
            break

        first = ORDER[i]
        second = ORDER[i + 1]

        for first_word in first:
            for second_word in second:
                if second_word.startswith(first_word):
                    if second_word in WHITELIST:
                        continue
                    starting_with_other_word.append((first_word, second_word))

    print(starting_with_other_word)
    assert len(starting_with_other_word) == 0


@pytest.mark.skip("Actually this is ok.")
def test_earlier_word_does_not_end_in_later_word():
    """Checks if a word is not an existing word with a suffix.But only checks this for words that can follow eachother in the hrid based on their order.

    Example:
        avoid `elegant-ant`
    """
    ending_with_later_word: list[tuple[str, str]] = []

    for i in range(len(ORDER) + 1):
        if i == len(ORDER) - 1:
            break

        first = ORDER[i]
        second = ORDER[i + 1]

        for first_word in first:
            for second_word in second:
                if first_word.endswith(second_word):
                    ending_with_later_word.append((first_word, second_word))

    print(ending_with_later_word)
    assert len(ending_with_later_word) == 0


@pytest.mark.skip("TODO")
def test_minimum_human_readable_part_length():
    """Check whether the minimum length of the human readable part is within bounds."""
    raise AssertionError()


@pytest.mark.skip("TODO")
def test_maximum_human_readable_part_length():
    """Check whether the maximum length of the human readable part is within bounds."""
    raise AssertionError()
