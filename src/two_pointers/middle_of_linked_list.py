# Middle of a Linked List
# Find the middle node of a linked list.

# Input: 0 1 2 3 4

# Output: 2

# If the number of nodes is even, then return the second middle node.

# Input: 0 1 2 3 4 5

# Output: 3


from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next


def find_middle_of_linked_list(head: Optional[Node]) -> int:
    slow: Optional[Node] = head
    fast: Optional[Node] = head
    while fast and fast.next:
        fast = fast.next.next
        if slow and slow.next:
            slow = slow.next
    if slow:
        return slow.value
    return -1
