def square_root(n: int) -> int:
    left, right = 0, n
    boundary_index = -1
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= n:
            boundary_index = mid
            left = mid + 1
        else:
            right = mid - 1
    return boundary_index


# Alias for compatibility with original name
square_rot = square_root
