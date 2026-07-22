import pytest

from src.two_pointers.three_sum import three_sum, threeSum


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([], []),
        ([1, 2], []),
        ([1, 2, 3, 4], []),
        ([-4, -3, -2, -1], []),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        (
            [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
            [
                [-4, -2, 6],
                [-4, 0, 4],
                [-4, 1, 3],
                [-4, 2, 2],
                [-2, -2, 4],
                [-2, 0, 2],
            ],
        ),
    ],
)
def test_three_sum(nums: list[int], expected: list[list[int]]) -> None:
    result = three_sum(nums)
    # Compare sorted triplets to ensure order invariance
    assert sorted([sorted(triplet) for triplet in result]) == sorted(
        [sorted(triplet) for triplet in expected]
    )


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_three_sum_alias(nums: list[int], expected: list[list[int]]) -> None:
    result = threeSum(nums)
    assert sorted([sorted(triplet) for triplet in result]) == sorted(
        [sorted(triplet) for triplet in expected]
    )
