import pytest

from src.sliding_windows.max_quantity_of_warehouse_parsels import (
    Solution,
    max_balanced_subarray_length,
    maxBalancedSubarrayLength,
)


@pytest.mark.parametrize(
    ("parcels", "k", "expected"),
    [
        ([1, 2, 1, 2, 3, 2, 2], 2, 4),
        ([0, 1, 2, 2, 2, 3], 1, 3),
        ([1, 1, 1, 1], 1, 4),
        ([], 2, 0),
        ([1, 2, 3], 0, 0),
        ([1, 2, 3], -1, 0),
        ([1, 2, 3, 4, 5], 5, 5),
        ([1, 2, 3, 4, 5], 10, 5),
        ([5, 5, 5, 2, 2, 3, 3, 3, 3], 2, 6),
        ([1], 1, 1),
    ],
)
def test_max_balanced_subarray_length(
    parcels: list[int], k: int, expected: int
) -> None:
    assert max_balanced_subarray_length(parcels, k) == expected


@pytest.mark.parametrize(
    ("parcels", "k", "expected"),
    [
        ([1, 2, 1, 2, 3, 2, 2], 2, 4),
        ([0, 1, 2, 2, 2, 3], 1, 3),
    ],
)
def test_max_balanced_subarray_length_alias(
    parcels: list[int], k: int, expected: int
) -> None:
    assert maxBalancedSubarrayLength(parcels, k) == expected


@pytest.mark.parametrize(
    ("parcels", "k", "expected"),
    [
        ([1, 2, 1, 2, 3, 2, 2], 2, 4),
        ([0, 1, 2, 2, 2, 3], 1, 3),
    ],
)
def test_solution_class(parcels: list[int], k: int, expected: int) -> None:
    solution = Solution()
    assert solution.maxBalancedSubarrayLength(parcels, k) == expected
