import pytest

from src.depth_first_search.tree_max_depth import Node, build_tree, tree_max_depth


def test_tree_max_depth_empty() -> None:
    assert tree_max_depth(None) == 0


def test_tree_max_depth_single_node() -> None:
    root = Node(1)
    assert tree_max_depth(root) == 0


def test_tree_max_depth_two_nodes() -> None:
    root = Node(1, left=Node(2))
    assert tree_max_depth(root) == 1


@pytest.mark.parametrize(
    ("tree_str", "expected"),
    [
        ("x", 0),
        ("0 x x", 0),
        ("5 3 x 4 x x 8 x x", 2),
        ("1 2 3 4 x x x x x", 3),
        ("1 2 3 x x 4 x x 5 x 6 x x", 2),
        ("-5 -10 x x -1 x x", 1),
        ("10 20 40 x x 50 x x 30 x 60 x x", 2),
    ],
)
def test_tree_max_depth_serialized(tree_str: str, expected: int) -> None:
    root = build_tree(iter(tree_str.split()), int)
    assert tree_max_depth(root) == expected


def test_tree_max_depth_unbalanced() -> None:
    # Right-skewed tree: 1 -> 2 -> 3 -> 4
    root = Node(1, right=Node(2, right=Node(3, right=Node(4))))
    assert tree_max_depth(root) == 3


def test_tree_max_depth_complex() -> None:
    # Left subtree depth 2, Right subtree depth 1
    left_subtree = Node(2, left=Node(4, left=Node(8)), right=Node(5))
    right_subtree = Node(3, right=Node(7))
    root = Node(1, left=left_subtree, right=right_subtree)
    # Longest path: 1 -> 2 -> 4 -> 8 (3 edges)
    assert tree_max_depth(root) == 3
