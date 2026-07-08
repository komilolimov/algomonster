# 1446. Consecutive Characters
# The power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Given a string s, return the power of s.


# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:

# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.


def max_power(s: str) -> int:
    left = 0
    result = 0
    for right in range(len(s)):
        if s[left] != s[right]:
            left = right
        result = max(result, right - left + 1)
    return result
