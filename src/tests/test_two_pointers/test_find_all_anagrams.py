import pytest
from src.two_pointers.find_all_anagrams import find_all_anagrams


@pytest.mark.parametrize(
    "original, check, expected",
    [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
        ("hello", "xyz", []),
        ("a", "ab", []),
        ("abc", "abc", [0]),
        ("aaaaa", "aa", [0, 1, 2, 3]),
        ("a", "a", [0]),
        ("bacbabc", "abc", [0, 1, 2, 4]),
    ],
)
def test_find_all_anagrams(original: str, check: str, expected: list[int]) -> None:
    assert find_all_anagrams(original, check) == expected
