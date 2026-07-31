# Subarray Sum Equals Target
# Given an integer array arr and a target value, return a subarray whose sum equals the target.
# Return the answer as [start, end), where start is inclusive and end is exclusive.
# If there are multiple valid answers, return the one with the smaller end value.


def subarray_sum(arr: list[int], target: int) -> list[int]:
    current_sum = 0
    prefix_map = {0: -1}
    for i, num in enumerate(arr):
        current_sum += num
        past_sum = current_sum - target
        if past_sum in prefix_map:
            start = prefix_map[past_sum] + 1
            end = i + 1
            return [start, end]
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i

    return []


# Alias for function name matching module/problem description
subarray_sum_target = subarray_sum
