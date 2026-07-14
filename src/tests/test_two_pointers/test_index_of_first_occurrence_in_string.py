import pytest

from src.two_pointers.index_of_first_occurrence_in_string import strStr


@pytest.mark.parametrize(
    "haystack, needle, expected",
    [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("", "a", -1),
        ("a", "", 0),
        ("mississippi", "issip", 4),
    ],
)
def test_str_str(haystack: str, needle: str, expected: int) -> None:
    assert strStr(haystack, needle) == expected
