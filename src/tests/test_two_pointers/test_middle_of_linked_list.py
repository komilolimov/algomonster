import pytest

from src.two_pointers.middle_of_linked_list import Node, find_middle_of_linked_list


def build_linked_list(values: list[int]) -> Node | None:
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


@pytest.mark.parametrize(
    ("input_values", "expected"),
    [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5, 6], 4),
    ],
)
def test_find_middle_of_linked_list(input_values: list[int], expected: int) -> None:
    head = build_linked_list(input_values)
    assert find_middle_of_linked_list(head) == expected
