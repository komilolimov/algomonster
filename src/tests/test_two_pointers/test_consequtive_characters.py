import pytest

from src.two_pointers.consequtive_characters import max_power


@pytest.mark.parametrize(
    "s, expected",
    [
        ("leetcode", 2),
        ("abbcccddddeeeeedcba", 5),
        ("", 0),
        ("a", 1),
        ("aaaa", 4),
        ("abcdef", 1),
        ("hooraaaaaaaaaay", 10),
        ("tourist", 1),
    ],
)
def test_max_power(s: str, expected: int) -> None:
    assert max_power(s) == expected
