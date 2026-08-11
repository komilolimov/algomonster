# 209. Minimum Size Subarray Sum
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# Constraints:
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).


def min_sub_array_len(target: int, nums: list[int]) -> int:
    left = 0
    current_window_sum = 0
    length = len(nums) + 1
    for right in range(len(nums)):
        current_window_sum += nums[right]
        while current_window_sum >= target:
            length = min(length, right - left + 1)
            current_window_sum -= nums[left]
            left += 1
    return length if length <= len(nums) else 0


# Aliases for LeetCode style / camelCase compatibility
minSubArrayLen = min_sub_array_len


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        return min_sub_array_len(target, nums)
