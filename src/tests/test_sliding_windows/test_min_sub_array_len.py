import pytest

from src.sliding_windows.min_sub_array_len import (
    Solution,
    min_sub_array_len,
    minSubArrayLen,
)


@pytest.mark.parametrize(
    ("target", "nums", "expected"),
    [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
        (5, [5], 1),
        (5, [10], 1),
        (5, [3], 0),
        (5, [], 0),
        (10, [1, 2, 3, 4], 4),
        (8, [1, 2, 3, 4, 5], 2),
        (100, [1, 2, 3, 4, 5], 0),
        (6, [2, 2, 2, 2], 3),
        (10, [10, 1, 1, 1], 1),
        (10, [1, 1, 1, 10], 1),
        (7, [2, 15, 3], 1),
    ],
)
def test_min_sub_array_len(target: int, nums: list[int], expected: int) -> None:
    assert min_sub_array_len(target, nums) == expected


@pytest.mark.parametrize(
    ("target", "nums", "expected"),
    [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
    ],
)
def test_min_sub_array_len_alias(target: int, nums: list[int], expected: int) -> None:
    assert minSubArrayLen(target, nums) == expected


@pytest.mark.parametrize(
    ("target", "nums", "expected"),
    [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
    ],
)
def test_solution_class(target: int, nums: list[int], expected: int) -> None:
    solution = Solution()
    assert solution.minSubArrayLen(target, nums) == expected
