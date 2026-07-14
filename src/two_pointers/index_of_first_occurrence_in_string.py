# 28. Find the Index of the First Occurrence in a String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# Dry Run Example 1:
# haystack = "sadbutsad", needle = "sad"
# len(haystack) = 9, len(needle) = 3
# range(len(haystack) - len(needle) + 1) -> range(0, 7)
# i = 0:
#   haystack[0:3] = "sad"
#   "sad" == "sad" -> True
#   return 0


def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
    