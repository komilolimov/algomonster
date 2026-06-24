import pytest
from typing import List, Optional
from src.two_pointers.middle_of_linked_list import find_middle_of_linked_list, Node


def build_linked_list(values: List[int]) -> Optional[Node]:
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


@pytest.mark.parametrize(
    "input_values, expected",
    [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5, 6], 4),
    ],
)
def test_find_middle_of_linked_list(input_values: List[int], expected: int) -> None:
    head = build_linked_list(input_values)
    assert find_middle_of_linked_list(head) == expected
