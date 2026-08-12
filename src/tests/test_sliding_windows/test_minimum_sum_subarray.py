import pytest

from src.sliding_windows.minimum_sum_subarray import (
    Solution,
    minimum_sum_subarray,
    minimumSumSubarray,
)


@pytest.mark.parametrize(
    ("nums", "l", "r", "expected"),
    [
        ([3, -2, 1, 4], 2, 3, 1),
        ([-2, 2, -3, 1], 2, 3, -1),
        ([1, 2, 3, 4], 2, 4, 3),
        ([-1, -2, -3], 1, 2, -1),
        ([-5, 10, -5], 1, 1, 10),
        ([5, -4, 2, -1, 3], 1, 3, 1),
        ([-2, 5, 3], 3, 3, 6),
        ([1, 2], 3, 4, -1),
        ([10, -8, 2, 3], 2, 3, 2),
        ([7], 1, 1, 7),
        ([-7], 1, 1, -1),
    ],
)
def test_minimum_sum_subarray(
    nums: list[int],
    l: int,
    r: int,
    expected: int,  # noqa: E741
) -> None:
    assert minimum_sum_subarray(nums, l, r) == expected


@pytest.mark.parametrize(
    ("nums", "l", "r", "expected"),
    [
        ([3, -2, 1, 4], 2, 3, 1),
        ([-2, 2, -3, 1], 2, 3, -1),
        ([1, 2, 3, 4], 2, 4, 3),
    ],
)
def test_minimum_sum_subarray_alias(
    nums: list[int],
    l: int,
    r: int,
    expected: int,  # noqa: E741
) -> None:
    assert minimumSumSubarray(nums, l, r) == expected


@pytest.mark.parametrize(
    ("nums", "l", "r", "expected"),
    [
        ([3, -2, 1, 4], 2, 3, 1),
        ([-2, 2, -3, 1], 2, 3, -1),
        ([1, 2, 3, 4], 2, 4, 3),
    ],
)
def test_solution_class(
    nums: list[int],
    l: int,
    r: int,
    expected: int,  # noqa: E741
) -> None:
    solution = Solution()
    assert solution.minimumSumSubarray(nums, l, r) == expected
