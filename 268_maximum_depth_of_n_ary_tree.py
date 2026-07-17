# 268. Maximum Depth of N-ary Tree
# Given a n-ary tree, find its maximum depth.

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def max_depth(root):
    if not root:
        return 0
    if not root.children:
        return 1
    return 1 + max(max_depth(child) for child in root.children)

if __name__ == "__main__":
    root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    print(max_depth(root))  # 3
