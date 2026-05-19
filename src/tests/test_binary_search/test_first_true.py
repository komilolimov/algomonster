import pytest
from src.binary_search.first_true import find_boundary


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([False, False, True, True, True], 2),
        ([True, True, True], 0),
        ([False, False, False], -1),
        ([False, True], 1),
        ([True], 0),
        ([False], -1),
        ([], -1),
    ],
)
def test_find_boundary(arr: list[bool], expected: int) -> None:
    assert find_boundary(arr) == expected
