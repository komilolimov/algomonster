import pytest
from src.binary_search.last_occurrence import last_occurrence


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([], 3, -1),
        ([2, 3, 5], 1, -1),
        ([2, 3, 5], 6, -1),
        ([2, 3, 5], 4, -1),
        ([5], 5, 0),
        ([5], 3, -1),
        ([5, 5, 5, 10, 15], 5, 2),
        ([1, 2, 5, 5, 5, 10, 15], 5, 4),
        ([1, 2, 5, 10, 15, 15], 15, 5),
        ([1, 2, 5, 10, 15], 5, 2),
        ([1, 3, 3, 3, 3, 6, 10, 10, 10, 100], 3, 4),
    ],
)
def test_last_occurrence(arr: list[int], target: int, expected: int) -> None:
    assert last_occurrence(arr, target) == expected
