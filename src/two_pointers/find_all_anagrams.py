# Find All Anagrams in a String
# Given a string original and a string check, find the starting index of all substrings in original that are anagrams of check. Return the indices in ascending order.

# Parameters
# original: A string
# check: A string
# Result
# A list of integers representing the starting indices of all anagrams of check.
# Examples
# Example 1
# Input: original = "cbaebabacd", check = "abc"

# Output: [0, 6]

# Explanation: original[0:3] = "cba" and original[6:9] = "bac" each contain exactly the same letters as "abc" with different ordering.

# Example 2
# Input: original = "abab", check = "ab"

# Output: [0, 1, 2]

# Explanation: Every length-2 window in "abab" ("ab", "ba", "ab") is an anagram of "ab".

# Constraints
# 1 <= len(original), len(check) <= 10^5
# Each string consists of only lowercase characters in the standard English alphabet.
from collections import Counter


def find_all_anagrams(original: str, check: str) -> list[int]:
    if len(check) > len(original):
        return []
    result = []
    check_count = Counter(check)
    window_count = Counter(original[: len(check)])
    if window_count == check_count:
        result.append(0)
    for i in range(len(check), len(original)):
        window_count[original[i]] += 1
        window_count[original[i - len(check)]] -= 1
        if window_count[original[i - len(check)]] == 0:
            del window_count[original[i - len(check)]]
        if window_count == check_count:
            result.append(i - len(check) + 1)
    return result
