import pytest
from src.binary_search.square_root_estimation import square_root, square_rot


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2),
        (8, 2),
        (9, 3),
        (10, 3),
        (15, 3),
        (16, 4),
        (99, 9),
        (100, 10),
        (101, 10),
        (10000, 100),
    ],
)
def test_square_root(n: int, expected: int) -> None:
    assert square_root(n) == expected
    assert square_rot(n) == expected
