def first_not_smaller(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            ans = mid
            right = mid - 1

        else:
            left = mid + 1
    return ans
