# Sliding Window Introduction
# Sliding window problems are a variant of the same direction two pointers problems. The function performs on the entire interval between the two pointers instead of only at the two positions. Usually, we keep track of the overall result of the window, and when we "slide" the window (insert/remove an item), we simply manipulate the result to accommodate the changes to the window. Time complexity wise, this is much more efficient as we do not recalculate the overlapping intervals between two windows over and over again. We try to reduce a nested loop into two passes on the input (one pass with each pointer).

# Fixed Size Sliding Window
# Given an array (list) nums consisted of only non-negative integers, find the largest sum among all subarrays of length k in nums.

# For example, if the input is nums = [1, 2, 3, 7, 4, 1], k = 3, then the output would be 14 as the largest length 3 subarray sum is given by [3, 7, 4] which sums to 14.

from typing import List


def subarray_sum_fixed(nums: List[int], k: int) -> int:
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
