# 15. 3Sum
# Medium
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


def three_sum(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = []
    nums.sort()
    for i, a in enumerate(nums):
        if a > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            three_sum_val = nums[left] + nums[right] + a
            if three_sum_val > 0:
                right -= 1
            elif three_sum_val < 0:
                left += 1
            else:
                res.append([a, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return res


# Alias for backward compatibility / LeetCode format
threeSum = three_sum
