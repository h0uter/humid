import statistics
import time
from collections.abc import Callable
from typing import TypeVar
from uuid import UUID, uuid4

from uniplot import histogram

from humid import hrid

T = TypeVar("T", UUID, str)  # Define a type variable that can be either UUID or str


def compare(uuids: list[T]) -> bool:
    for i in range(len(uuids)):
        for j in range(i + 1, len(uuids)):
            if uuids[i] == uuids[j]:
                print("Oh no collision")
                return False

    return True


def obtain_durations(
    uuid_constructor: Callable[[], T],
    nr_uuids: int,
    n_experiments: int,
    verbose=False,
) -> float:
    uuids = [uuid_constructor() for _ in range(nr_uuids)]
    durations = []

    # Perform pairwise comparison
    for i in range(n_experiments):
        if verbose:
            print(f"Starting experiment {i}", end="\r")

        start = time.perf_counter()
        compare(uuids)
        end = time.perf_counter()

        duration = end - start
        durations.append(duration)

    avg_duration = statistics.mean(durations)

    if verbose:
        print()
        print(f"Average duration: {avg_duration}")

        histogram(
            durations,
            bins_min=min(durations),
            bins_max=max(durations),
            title=f"Duration Histogram {n_experiments} samples and {nr_uuids} UUIDS",
            x_unit="Sec",
            y_unit="#",
        )
    return avg_duration


def test_hrid_comparison_faster_than_uuid4():
    """Test comparison of hrids is same speed as uuid4"""
    uuid4_avg_duration = obtain_durations(
        uuid_constructor=uuid4, nr_uuids=1000, n_experiments=100
    )
    hrid_avg_duration = obtain_durations(
        uuid_constructor=hrid, nr_uuids=1000, n_experiments=100
    )

    print(f"uuid4 avg duration: {uuid4_avg_duration}")
    print(f"hrid avg duration: {hrid_avg_duration}")

    assert hrid_avg_duration <= uuid4_avg_duration


test_hrid_comparison_faster_than_uuid4()
