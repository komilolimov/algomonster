# 📦 Amazon Logistics: Maximum Quality of Warehouse ParcelsProblem Statement:Amazon's fulfillment center arranges parcels in a long line,
#  represented by an array of integers parcels, where parcels[i] represents the category ID of the $i$-th parcel.
# A section of the line is considered "Balanced" if:The number of distinct parcel categories in that section is at most $K$
# .Write a function maxBalancedSubarrayLength(parcels, k) that returns the maximum length of a contiguous section (subarray) of parcels
# that is Balanced.


# Example 1:
# Input: parcels = [1, 2, 1, 2, 3, 2, 2], k = 2
# Output: 5
# Explanation:
# The longest valid contiguous section with at most 2 distinct categories is [1, 2, 1, 2] or [2, 3, 2, 2].
# The longest length is 5: subarray [2, 1, 2, 3, 2, 2] is invalid because it has 3 distinct elements (1, 2, 3).
# Subarray [2, 3, 2, 2] has length 4, but [1, 2, 1, 2] has length 4... Wait!
# Look at [1, 2, 1, 2] -> 2 distinct elements (1, 2), length = 4.
# Look at [2, 3, 2, 2] -> 2 distinct elements (2, 3), length = 4.
# Wait, what about [2, 1, 2]? Length 3.
# Therefore, max length with at most 2 distinct elements is 4.


# Example 2:
# Input: parcels = [0, 1, 2, 2, 2, 3], k = 1
# Output: 3
# Explanation:
# With k = 1, we can only have 1 distinct category.
# The longest contiguous section with 1 distinct element is [2, 2, 2], which has length 3.


def max_balanced_subarray_length(parcels: list[int], k: int) -> int:
    if k <= 0 or not parcels:
        return 0
    left = 0
    max_length = 0
    frequency: dict[int, int] = {}
    for right, val in enumerate(parcels):
        frequency[val] = frequency.get(val, 0) + 1
        while len(frequency) > k:
            left_val = parcels[left]
            frequency[left_val] -= 1
            if frequency[left_val] == 0:
                del frequency[left_val]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length


# Aliases for LeetCode / camelCase compatibility
maxBalancedSubarrayLength = max_balanced_subarray_length


class Solution:
    def maxBalancedSubarrayLength(self, parcels: list[int], k: int) -> int:
        return max_balanced_subarray_length(parcels, k)
