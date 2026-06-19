from typing import List


# arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
# target = 3


def last_occurrence(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            boundary_index = mid
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index
