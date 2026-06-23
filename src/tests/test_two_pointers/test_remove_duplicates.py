import pytest
from src.two_pointers.remove_duplicates import remove_duplicates


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([0, 0, 1, 1, 1, 2, 2], 3),
        ([0, 0, 1, 1, 1, 2, 2], 3),
        ([1, 2, 3, 4, 5], 5),
        ([1, 1, 1, 1, 1], 1),
        ([1], 1),
    ],
)
def test_remove_duplicates(arr: list[int], expected: int) -> None:
    assert remove_duplicates(arr) == expected
