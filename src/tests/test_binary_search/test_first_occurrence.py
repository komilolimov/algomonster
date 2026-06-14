import pytest
from src.binary_search.first_occurrence import find_first_occurrence


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([], 3, -1),
        ([2, 3, 5], 1, -1),
        ([2, 3, 5], 6, -1),
        ([2, 3, 5], 4, -1),
        ([5], 5, 0),
        ([5], 3, -1),
        ([5, 5, 5, 10, 15], 5, 0),
        ([1, 2, 5, 5, 5, 10, 15], 5, 2),
        ([1, 2, 5, 10, 15, 15], 15, 4),
        ([1, 2, 5, 10, 15], 5, 2),
    ],
)
def test_find_first_occurrence(arr: list[int], target: int, expected: int) -> None:
    assert find_first_occurrence(arr, target) == expected
