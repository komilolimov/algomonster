import pytest
from src.two_pointers.middle_of_linked_list import find_middle_of_linked_list

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

@pytest.mark.parametrize("input_values, expected", [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4, 5, 6], 4),
])
def test_find_middle_of_linked_list(input_values, expected):
    head = build_linked_list(input_values)
    assert find_middle_of_linked_list(head) == expected