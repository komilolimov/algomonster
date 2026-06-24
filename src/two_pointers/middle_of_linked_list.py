# Middle of a Linked List
# Find the middle node of a linked list.

# Input: 0 1 2 3 4

# Output: 2

# If the number of nodes is even, then return the second middle node.

# Input: 0 1 2 3 4 5

# Output: 3


def find_middle_of_linked_list(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.value
