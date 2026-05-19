import pytest
from src.binary_search.bigger_target import first_not_smaller


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 3, 3, 5, 8, 8, 10], 2, 1),
        ([1, 3, 3, 5, 8, 8, 10], 8, 4),
        ([1, 3, 3, 5, 8, 8, 10], 1, 0),
        ([1, 3, 3, 5, 8, 8, 10], 10, 6),
        ([1, 3, 3, 5, 8, 8, 10], 11, -1),
        ([1, 3, 3, 5, 8, 8, 10], 0, 0),
        ([5], 5, 0),
        ([5], 3, 0),
        ([5], 7, -1),
        ([], 3, -1),
    ],
)
def test_first_not_smaller(arr: list[int], target: int, expected: int):
    assert first_not_smaller(arr, target) == expected
