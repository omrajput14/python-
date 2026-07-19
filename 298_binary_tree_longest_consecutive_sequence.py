# 298. Binary Tree Longest Consecutive Sequence
# Given the root of a binary tree, return the length of the longest consecutive sequence path.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longest_consecutive(root):
    max_len = 0
    def dfs(node, parent_val, length):
        nonlocal max_len
        if not node: return
        if node.val == parent_val + 1:
            length += 1
        else:
            length = 1
        max_len = max(max_len, length)
        dfs(node.left, node.val, length)
        dfs(node.right, node.val, length)
    
    if not root: return 0
    dfs(root, root.val - 1, 0)
    return max_len

if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(3, TreeNode(2), TreeNode(4, None, TreeNode(5))))
    print(longest_consecutive(root))
