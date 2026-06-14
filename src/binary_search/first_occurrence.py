from typing import List

def find_first_occurrence(arr: List[int],  target: int) -> int:
    left, right = 0, len(arr) - 1
    first_occurrence = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            first_occurrence = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first_occurrence