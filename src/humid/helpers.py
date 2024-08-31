def probability_of_duplicate(list_lists_of_words: list[list[str]]):
    lengths = []
    odds = 1
    for list in list_lists_of_words:
        lengths.append(len(list))

    for length in lengths:
        odds *= 1 / length

    return odds


def one_in_XXXXX_chance_of_duplicate(list_lists_of_words: list[list[str]]):
    lengths = []
    odds = 1
    for list in list_lists_of_words:
        lengths.append(len(list))

    for length in lengths:
        odds *= 1 / length

    one_in_x = 1 / odds
    one_in_x_rounded = int(round(one_in_x))

    return one_in_x_rounded
