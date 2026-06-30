import pytest

from src.two_pointers.subarray_sum import subarray_sum_fixed


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3, 7, 4, 1], 3, 14),
        ([1, 2, 3, 7, 4, 1], 2, 11),
        ([1, 2, 3, 7, 4, 1], 6, 18),
        ([100], 1, 100),
        ([0, 0, 0, 0], 2, 0),
        ([4, 5, 6], 1, 6),
    ],
)
def test_subarray_sum_fixed(nums: list[int], k: int, expected: int) -> None:
    assert subarray_sum_fixed(nums, k) == expected
