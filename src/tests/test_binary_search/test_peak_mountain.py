import pytest
from src.binary_search.peak_mountain import (
    Solution,
    peak_index_in_mountain_array,
    peakIndexInMountainArray,
)


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([0, 1, 0], 1),
        ([0, 2, 1, 0], 1),
        ([0, 10, 5, 2], 1),
        ([0, 1, 2, 3, 4, 3, 2, 1, 0], 4),
        ([3, 4, 5, 1], 2),
        ([24, 69, 100, 99, 79, 78, 67, 36, 26, 19], 2),
        ([1, 3, 5, 4, 2], 2),
        ([0, 5, 10, 2], 2),
    ],
)
def test_peak_index_in_mountain_array(arr: list[int], expected: int) -> None:
    sol = Solution()
    assert sol.peakIndexInMountainArray(arr) == expected
    assert peak_index_in_mountain_array(arr) == expected
    assert peakIndexInMountainArray(arr) == expected
