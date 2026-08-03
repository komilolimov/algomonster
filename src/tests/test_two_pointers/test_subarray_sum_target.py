import pytest

from src.two_pointers.subarray_sum_target import subarray_sum, subarray_sum_target


@pytest.mark.parametrize(
    ("arr", "target", "expected"),
    [
        ([1, -20, -3, 30, 5, 4], 7, [1, 4]),
        ([1, 2, 3, 4], 6, [0, 3]),
        ([5], 5, [0, 1]),
        ([1, 2, 3], 10, []),
        ([], 5, []),
        ([10, -5, -2, 7, 3], 0, [1, 4]),
        ([3, 4, 7, 2, -3], 7, [0, 2]),
        ([0, 0, 0], 0, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [1, 4]),
    ],
)
def test_subarray_sum(arr: list[int], target: int, expected: list[int]) -> None:
    assert subarray_sum(arr, target) == expected


@pytest.mark.parametrize(
    ("arr", "target", "expected"),
    [
        ([1, -20, -3, 30, 5, 4], 7, [1, 4]),
        ([3, 4, 7, 2, -3], 7, [0, 2]),
        ([], 5, []),
    ],
)
def test_subarray_sum_target(arr: list[int], target: int, expected: list[int]) -> None:
    assert subarray_sum_target(arr, target) == expected
