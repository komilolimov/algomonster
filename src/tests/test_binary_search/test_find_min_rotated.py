import pytest
from src.binary_search.find_min_rotated import find_min_rotated


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([30, 40, 50, 10, 20], 3),
        ([3, 5, 7, 11, 13, 17, 19, 2], 7),
        ([10, 20, 30, 40, 50], 0),
        ([20, 30, 40, 50, 10], 4),
        ([10], 0),
        ([10, 20], 0),
        ([20, 10], 1),
    ],
)
def test_find_min_rotated(arr: list[int], expected: int) -> None:
    assert find_min_rotated(arr) == expected
