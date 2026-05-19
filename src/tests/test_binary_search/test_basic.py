import pytest
from src.binary_search.basic import binary_search


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 6, -1),
        ([1, 2, 3, 4, 5], 0, -1),
        ([], 3, -1),
        ([5], 5, 0),
        ([5], 3, -1),
        ([-10, -5, 0, 5, 10], -5, 1),
    ],
)
def test_binary_search(arr: list[int], target: int, expected: int) -> None:
    assert binary_search(arr, target) == expected
