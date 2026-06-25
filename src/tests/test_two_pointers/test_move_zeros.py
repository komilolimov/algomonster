import pytest

from src.two_pointers.move_zeros import move_zeros


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 0, 2, 0, 0, 7], [1, 2, 7, 0, 0, 0]),
        ([0], [0]),
        ([0, 0], [0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([], []),
    ],
)
def test_move_zeros(nums: list[int], expected: list[int]) -> None:
    move_zeros(nums)
    assert nums == expected
