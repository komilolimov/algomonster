# Max depth of a binary tree
# Prerequisite: DFS on Tree

# Max depth of a binary tree is the longest root-to-leaf path.
# Given a binary tree, find its max depth.
# Here, we define the length of the path to be the number of edges on that path, not the number of nodes.

from collections.abc import Callable, Iterator
from typing import Any


class Node:
    def __init__(
        self,
        val: Any,
        left: "Node | None" = None,
        right: "Node | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def tree_max_depth(root: Node | None) -> int:
    """Calculate the maximum depth (number of edges on longest root-to-leaf path) of a binary tree."""
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0

    left_depth = tree_max_depth(root.left) if root.left else -1
    right_depth = tree_max_depth(root.right) if root.right else -1

    return 1 + max(left_depth, right_depth)


def build_tree(nodes: Iterator[str], f: Callable[[str], Any]) -> Node | None:
    """Build a binary tree from a serialized iterator of node values."""
    val = next(nodes, "x")
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == "__main__":
    import sys

    input_data = sys.stdin.read().split()
    if input_data:
        root = build_tree(iter(input_data), int)
        res = tree_max_depth(root)
        print(res)
