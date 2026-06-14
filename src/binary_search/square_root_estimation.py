# Given an integer, find its square root without using the built-in square root function. Only return the integer part (truncate the decimals).

# Input: 16

# Output: 4

# Input: 8

# Output: 2

# Explanation: square root of 8 is 2.83..., return the integer part, 2


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
