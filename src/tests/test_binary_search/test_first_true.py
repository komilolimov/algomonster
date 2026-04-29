import pytest
from src.binary_search.first_true import find_boundary


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([False, False, True, True, True], 2),  # Граница в середине
        ([True, True, True], 0),  # Все True (граница в начале)
        ([False, False, False], -1),  # Все False (границы нет)
        ([False, True], 1),  # Граница из двух элементов
        ([True], 0),  # Один элемент, True
        ([False], -1),  # Один элемент, False
        ([], -1),  # Пустой массив
    ],
)
def test_find_boundary(arr: list[bool], expected: int):
    assert find_boundary(arr) == expected
