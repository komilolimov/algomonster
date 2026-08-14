from src.depth_first_search.tree_max_depth import Node, build_tree, tree_max_depth

__all__ = ["Node", "tree_max_depth", "build_tree"]

if __name__ == "__main__":
    import sys

    input_data = sys.stdin.read().split()
    if input_data:
        root = build_tree(iter(input_data), int)
        res = tree_max_depth(root)
        print(res)
