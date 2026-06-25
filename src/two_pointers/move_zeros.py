# Move Zeros
# Given an array of integers, move all the 0s to the back of the array while maintaining the relative order of the non-zero elements. Do this in-place using constant auxiliary space.

# Input:

# [1, 0, 2, 0, 0, 7]
# Output:

# [1, 2, 7, 0, 0, 0]


from typing import List


def move_zeros(nums: List[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
